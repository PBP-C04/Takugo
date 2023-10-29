async function getBookList(filter) {
    return fetch(`api/book-list?filter=${filter}`)
        .then((res) => res.json());
}

async function getBoughtBook(filter) {
    return fetch(`api/book-bought?filter=${filter}`)
        .then((res) => res.json());
}

async function refreshList(books, all) {
    const BOOK_TYPES = {
        "MGA": "Manga",
        "LNV": "Light-Novel",
        "DJS": "Doujinshi",
        "MHW": "Manhwa",
        "MHU": "Manhua",
        "NVL": "Novel",
        "OTH": "Other"
    }

    document.getElementById("list").innerHTML = "";
    let htmlString = "";
    books.forEach((book) => {
        const addJournalButton = document.createElement("a");
        addJournalButton.href = `show_journal/${book.pk}/`;
        addJournalButton.classList.add("btn", "btn-outline-warning");
        addJournalButton.textContent = "Add Journal";

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
                            <div class="add-journal-button">${addJournalButton.outerHTML}</div>
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
refreshBookList("none", "all");