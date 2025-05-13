document.getElementById('openViewer').addEventListener('click', async () => {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (!file) {
        alert('Please select a file.');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch('http://127.0.0.1:5000/upload', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    if (result.error) {
        alert(result.error);
        return;
    }

    chrome.tabs.create({
        url: chrome.runtime.getURL('viewer.html') + `?file=${result.filename}&type=${result.type}`
    });
});
