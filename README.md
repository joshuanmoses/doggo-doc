<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>
  <h1>Doggo-Doc: Veterinary Diagnosis Assistant</h1>
  <p><strong>Author:</strong> Joshua N. Moses</p>

  <h2>Overview</h2>
  <p>Doggo-Doc is an AI-powered assistant designed to aid in veterinary diagnostics. It leverages a custom GPT model trained on a LLaMA LLM, incorporating veterinary literature to provide informed diagnostic suggestions.</p>

  <h2>Features</h2>
  <ul>
    <li>Custom GPT model fine-tuned for veterinary applications</li>
    <li>Integration of veterinary literature in PDF format</li>
    <li>Interactive diagnostic assistance through natural language processing</li>
  </ul>

  <h2>Installation</h2>
  <ol>
    <li>Clone the repository:
      <pre><code>git clone https://github.com/joshuanmoses/doggo-doc.git</code></pre>
    </li>
    <li>Navigate to the project directory:
      <pre><code>cd doggo-doc</code></pre>
    </li>
    <li>Install the required dependencies:
      <pre><code>pip install -r requirements.txt</code></pre>
    </li>
  </ol>

  <h2>Usage</h2>
  <p>To start the diagnostic assistant, run:</p>
  <pre><code>python doggo_doc.py</code></pre>
  <p>Follow the on-screen prompts to input symptoms or queries related to veterinary diagnostics.</p>

  <h2>Project Structure</h2>
  <ul>
    <li><code>doggo_doc.py</code>: Main script to initiate the diagnostic assistant</li>
    <li><code>Instructions.py</code>: Contains instructions or guidelines for using the assistant</li>
    <li><code>vet1.pdf</code>, <code>vet2.pdf</code>, <code>vet3.pdf</code>: Veterinary literature used for model training or reference</li>
  </ul>


</body>
</html>
