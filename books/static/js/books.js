async function getBookList(filter) {
    return fetch(`api/book-list?filter=${filter}`)
        .then((res) => res.json());
}

async function getBoughtBook(filter) {
    return fetch(`api/book-bought?filter=${filter}`)
        .then((res) => res.json());
}

async function refreshList(books, all) {
    document.getElementById("list").innerHTML = "";
    all = all === "all";
    let htmlString = "";
    books.forEach((book) => {
        let button = document.createElement("button");
        button.textContent = "Buy";
        button.style.display = "block-inline";
        button.type = "button";
        button.className = "btn btn-outline-warning";
        button.setAttribute("data-bs-toggle", "modal");
        button.setAttribute("data-bs-target", "#buyModal");
        button.setAttribute("onclick", `showModal(${JSON.stringify(book)})`);
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
                            ${all ? "" : `<h6 class="card-subtitle mb-2 text-muted">Amount: ${book.fields.amount}</h6>`}
                            ${all ? button.outerHTML : ""}
                        </div>
                    </div>
                </div>
            </div>
        `;
    });
    document.getElementById("list").innerHTML = htmlString;
}

async function refreshBookList(filter, all) {
    if (filter !== undefined) {
        all = document.getElementById("book-bought").value;
    } else if (all !== undefined) {
        filter = document.getElementById("filter").value;
    }
    const books = all === "all" ? await getBookList(filter) : await getBoughtBook(filter);
    refreshList(books, all);
}

function showModal(book) {
    document.getElementById("buyModalLabel").innerHTML = `Buy "${book.fields.title}"?`;
    
    let imgElement = document.getElementById("modal_book_cover");
    imgElement.src = book.fields.image_url;
    imgElement.alt = `${book.fields.title} Cover Image`;

    document.getElementById("buy_button").setAttribute("onclick", `buyBook(${JSON.stringify(book)})`);
    return false;
}

function buyBook(book) {
    fetch(`buy-book/${book.pk}`, {
        method: "POST",
        body: new FormData(document.querySelector("#form"))
    }).then((res) => {
        if (res.status === 403) {
            document.getElementById("toggleAlertModal").click();
        }
    });
}

refreshBookList("none", "all");
