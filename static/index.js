document.addEventListener("DOMContentLoaded", () => {
    button = document.querySelector("#shorten_button");
    button.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();
        updatePage()
    })

    document.addEventListener("click", copy);
});

function copy(event) {
    const element = event.target;
    if (element.id == "copy_shortened_url" || element.tagName == 'I'){
        const url = document.querySelector("#shortened_url");
        navigator.clipboard.writeText(url.textContent);
    }
}

async function updatePage() {
    const currentUrl = window.location.href;
    const longUrl = document.querySelector("#long-url").value;
    const formData = new FormData();
    formData.append("url", longUrl)
    try {
        const response = await fetch(currentUrl, {
            method: "POST",
            body: formData
        });
        if (!response.ok) {
          throw new Error(`Response status: ${response.status}`);
        }
    
        const html = await response.text();
        const pageContent = document.querySelector("#response");
        pageContent.innerHTML = html;
    } catch (error) {
        console.error(error);
    }
}