const params = new URLSearchParams(window.location.search);
const filename = params.get('file');
const fileType = params.get('type');
let currentPage = 1;

async function loadPage(pageNum) {
    const response = await fetch(`http://127.0.0.1:5000/${fileType}/${filename}/${pageNum}`);
    const data = await response.json();
    document.getElementById('page1').innerHTML = data.content;
    document.getElementById('page2').innerHTML = data.content;
}

document.getElementById('prev').addEventListener('click', () => {
    if (currentPage > 1) {
        currentPage -= 2;
        loadPage(currentPage);
    }
});

document.getElementById('next').addEventListener('click', () => {
    currentPage += 2;
    loadPage(currentPage);
});

loadPage(currentPage);
