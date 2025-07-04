# article_intent_resolver.py

from framework_models import Article, Intent
from shared_intent_utility import resolve_conflict_between_intents

class ArticleIntentResolver:
    def __init__(self, article_registry):
        self.articles = article_registry  # Dictionary: {article_id: Article}

    def get_intents_for_article(self, article_id):
        article = self.articles.get(article_id)
        if not article:
            raise ValueError(f"Article '{article_id}' not found in registry.")
        return article.intents

    def evaluate_article_with_context(self, article_id, context):
        """
        Evaluates an article's intents in light of a specific ethical context.
        """
        intents = self.get_intents_for_article(article_id)
        evaluations = []
        for intent in intents:
            result = intent.evaluate(context)
            evaluations.append({
                "intent_id": intent.id,
                "outcome": result.outcome,
                "confidence": result.confidence,
                "rationale": result.rationale
            })
        return evaluations

    def resolve_conflicting_articles(self, article_ids, context):
        """
        Compares multiple articles and their intents to generate a harmonized ethical stance.
        """
        all_evaluations = {
            aid: self.evaluate_article_with_context(aid, context) for aid in article_ids
        }

        # Flatten and consolidate all intents for unified resolution
        intents_grouped = [intent for evals in all_evaluations.values() for intent in evals]
        resolved = resolve_conflict_between_intents(intents_grouped)
        return resolved