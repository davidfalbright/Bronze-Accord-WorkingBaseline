import sys, json, yaml

def compile_reservoir(schema_file, answers_file, output_file):
    with open(schema_file) as f:
        schema = yaml.safe_load(f)
    with open(answers_file) as f:
        answers = json.load(f)

    reservoirs = { "root": [], "domain": [], "response": [], "experiential": [] }

    for qid, rule in schema["questions"].items():
        if qid not in answers:
            continue
        answer = answers[qid]
        belief = { "type": rule["type"], "weight": rule.get("default_weight", 1.0) }

        if "weight_map" in rule and isinstance(answer, int):
            belief["weight"] = rule["weight_map"].get(answer, rule.get("default_weight", 1.0))

        if "map" in rule and isinstance(answer, str):
            belief["content"] = rule["map"].get(answer, f"Unmapped answer: {answer}")
        elif rule.get("multiple", False) and isinstance(answer, list):
            for item in answer:
                b = belief.copy()
                b["content"] = rule["content_template"].format(item=item, text=item)
                reservoirs[rule["reservoir"]].append(b)
            continue
        else:
            if isinstance(answer, (str, int, float)):
                belief["content"] = rule["content_template"].format(text=answer, item=answer)
        
        reservoirs[rule["reservoir"]].append(belief)

    with open(output_file, "w") as f:
        yaml.dump(reservoirs, f, sort_keys=False)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python compiler.py schema.yaml answers.json reservoir.yaml")
    else:
        compile_reservoir(sys.argv[1], sys.argv[2], sys.argv[3])
