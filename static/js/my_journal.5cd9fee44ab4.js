var id="{{ book.pk }}";
var journalAdded = false;

async function checkJournalStatus() {
    const journals = await getJournal();
    journalAdded = journals.length > 0;
    if (journalAdded) {
        document.getElementById("start-journal-button").style.display = "none";
    }
    else {
        document.getElementById("start-journal-button").style.display = "block";
    }
}
checkJournalStatus();

async function getJournal() {
    return fetch("{% url 'journal:get_journal_json' id=0 %}".replace("0", id)).then((res) => res.json());
}

async function refreshJournal() {
    checkJournalStatus();
    const container = document.getElementById("item-cards");
    container.innerHTML = ""; 

    const journals = await getJournal();
    if (journals.length === 0) {
        container.innerHTML = `<div class="no-entry"> You haven't add anything yet:( </div>`
    } else {
        journals.forEach(journal => {
        const card = document.createElement("div");
        card.innerHTML = `
            <div class="journal-body">
                <div class="row">
                    <div class="col-6 date-added">🎎Date Added: ${journal.fields.date_added}</div>
                </div>
                <br>
                <div class="rating" id="starRating">
                    Rating: <span id="starIcons">${getStarIcons(journal.fields.rating)}</span>
                </div>
                <br>
                <div class="notes">📝Notes 
                    <br>
                </div>
                <div class="notes-body">${journal.fields.notes}</div>
                <br>
                <div class="favorite-quotes">🎌Favorite Quotes
                    <br>
                </div>
                <div class="favorite-quotes-body">${journal.fields.favorite_quotes}</div>
            </div>
        `;
        container.appendChild(card);
    });
    }
}
refreshJournal();

async function deleteJournal() {
    if (journalAdded) {
        // Menampilkan modal konfirmasi delete
        $('#deleteConfirmationModal').modal('show');
    } else {
        $('#deleteUnsuccessfulConfirmationModal').modal('show');
    }
}    

function confirmDeleteJournal() {
    fetch("{% url 'journal:delete_journal' id=0 %}".replace("0", id)).then((res) => {
        res.json();
        journalAdded = false;
        refreshJournal();
    });
}

function addJournal() {
    fetch("{% url 'journal:add_journal' id=0 %}".replace("0", id),  {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(() => {
        refreshJournal();
        document.getElementById("form").reset();
    });
    return false
}
document.getElementById("button_add").onclick = addJournal

function getStarIcons(rating) {
    const starIcon = '★'; // Unicode star character

    let starIcons = '';
    for (let i = 0; i < rating; i++) {
        starIcons += starIcon;
    }

    return starIcons;
}