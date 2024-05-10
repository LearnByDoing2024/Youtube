html_report = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ChatGPT Usage Report</title>
<style>
    body { font-family: Arial, sans-serif; line-height: 1.6; }
    .container { width: 80%; margin: auto; padding: 20px; }
    h1, h2 { color: #333366; }
    h1 { text-align: center; }
    ul { margin: 20px; }
    li { margin: 10px 0; }
</style>
</head>
<body>
<div class="container">
    <h1>Pros and Cons of Using ChatGPT</h1>

    <h2>Pros of Using ChatGPT</h2>
    <ul>
        <li><strong>Inspiration and Idea Generation:</strong> Serves as a brainstorming tool, helping structure and generate ideas.</li>
        <li><strong>External Reference Capabilities:</strong> Can refer to external resources, enhancing information relevance and accuracy.</li>
        <li><strong>Customization and Query Mechanism:</strong> Users can customize GPT for specific tasks and fine-tune outputs using prompt engineering.</li>
    </ul>

    <h2>Cons of Using ChatGPT</h2>
    <ul>
        <li><strong>Usage Limits:</strong> Usage caps on GPT-4 model; may require downgrading or waiting when exceeded.</li>
        <li><strong>Hidden Computational Limits:</strong> Sometimes less detailed to save resources, limiting complex outputs.</li>
        <li><strong>Recursive Improvement Challenges:</strong> Struggles to continuously improve specific content like coding beyond a certain point.</li>
        <li><strong>Outdated Information:</strong> Relies on data up to its last update, lacking in current details.</li>
        <li><strong>Personalized GPT Limitations:</strong> Personalized GPTs might also provide generic short answers, minimizing computational demands.</li>
    </ul>

    <h2>Recommendations</h2>
    <ul>
        <li><strong>Multiple Models:</strong> Use multiple online, offline models to improve solution to a problem.</li>
        <li><strong>RAG:</strong> RAG, and other strategies to improve prompt and query mechnism</li>
    </ul>
</div>
</body>
</html>
"""

with open("ChatGPT_Presentation.html", "w") as file:
    file.write(html_report)

print("HTML file has been created successfully!")
