async function getBookList(filter) {
    return fetch(`api/book-list?filter=${filter}`)
        .then((res) => res.json());
}

async function refreshList(filter) {
    const books = await getBookList(filter);
    document.getElementById("list").innerHTML = "";
    let htmlString = ``;
    books.forEach((book) => {
        let button = document.createElement("button");
        button.textContent = "Show Review";
        button.style.display = "block-inline";
        button.type = "button";
        button.className = "btn btn-outline-warning";
        const showReviewUrl = `show-bookreview/${book.pk}`;
        button.setAttribute("onclick", `window.location.href='${showReviewUrl}'`);
        htmlString += `
            <div class="card mb-3" style="width: 25rem; display: inline-block;">
                <div class="row g-0">
                    <div class="col-md-4">
                        <img src=${book.fields.image_url} class="img-fluid rounded-start" alt="${book.fields.title} Cover Image" width="200" height="280">
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <h5 class="card-title">${book.fields.title}</h5>
                            <h6 class="card-subtitle mb-2 text-muted">Score: ${book.fields.score}</h6>
                            <h6 class="card-subtitle mb-2 text-muted">Volumes: ${book.fields.volumes}</h6>
                            ${button.outerHTML}
                        </div>
                    </div>
                </div>
            </div>
        `;
    });
    
    // htmlString += "</tbody>"
    document.getElementById("list").innerHTML = htmlString;
}

refreshList("none");
