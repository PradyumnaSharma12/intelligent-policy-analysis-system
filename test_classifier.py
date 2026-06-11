from app.utils.classifier_service import classify_text

sample_text = """
NASA announced a new Mars mission
to study the atmosphere of the planet.
"""

print(classify_text(sample_text))
