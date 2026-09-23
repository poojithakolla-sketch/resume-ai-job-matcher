import re


def clean_text(text):
    """
    Clean and normalize resume text.
    """

    # Convert to lowercase
    text = text.lower()

    # Normalize important technical symbols
    text = text.replace("c++", "cpp")
    text = text.replace("c#", "csharp")
    text = text.replace(".net", "dotnet")

    # Remove unnecessary special characters
    text = re.sub(r"[^a-zA-Z0-9+#.\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()