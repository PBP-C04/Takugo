// bookreview.js
var ratingInput = document.getElementById('rating');
var ratingOutput = document.getElementById('ratingValue');
var reviewList = document.getElementById('review_list');
var form = document.getElementById('form');

// Function to get reviews
async function getReview() {
    return fetch(`review-json/${book_id}`)
        .then((res) => res.json());
}

// Function to refresh reviews
async function refreshReview() {
    reviewList.innerHTML = "";

    const reviews = await getReview();

    reviews.forEach((review) => {
        const listItem = document.createElement("li");
        listItem.classList.add("list-group-item");
        listItem.innerHTML = `
        <div class="card mb-3" style="width: 25rem; display: inline-block; border: 1px solid #ccc; border-radius: 10px; padding: 10px; margin: 10px; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); transition: 0.3s; background-color: #f8f9fa;">
            <div class="col-md-4">
                <div class="card-body">
                    <div class="review" style="display: flex; justify-content: center; align-items: center;">
                        <div class="rating" style="text-align: left; margin: 5px;">
                            <p style="font-size: 16px;">User rating : ${review.fields.rating}</p>
                        </div>
                        <div class="comment" style="text-align: center; font-size: 16px; margin: 10px;">
                            ${review.fields.comment}
                        </div>
                        <div class="posted-at" style="text-align: left; margin: 2px;">
                            <p>Posted at: ${review.fields.date_added}</p>
                        </div>
                        <div class="delete" style="text-align: left; margin: 2px;">
                            <a href="javascript:void(0)" onclick="deleteReview(${review.pk})">Delete Review</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        `;
        reviewList.appendChild(listItem);
    });
}


// Function to add a review
function addReview() {
    fetch(`add-review/${book_id}`, {
        method: "POST",
        body: new FormData(form)
    }).then(() => {
        refreshReview();
        updateDataCount();
        form.reset();
    });
    return false;
}

// Function to delete a review
function deleteReview(id) {
    if (userType === "U") {
        const deleteReviewConfirmationModal = new bootstrap.Modal(document.getElementById('deleteReviewConfirmationModal'));
        const unauthorizedDeleteModal = new bootstrap.Modal(document.getElementById('unauthorizedDeleteModal'));

        deleteReviewConfirmationModal.show();
        document.getElementById('confirmDeleteReviewButton').onclick = () => {
            fetch(`delete-review/${id}`, {
                method: "POST",
                body: new FormData(form)
            })
            .then(response => {
                if (response.status === 200) {
                    updateDataCount();
                    refreshReview();
                    form.reset();
                } else if (response.status === 403) {
                    unauthorizedDeleteModal.show();
                }
            })
            .catch(error => {
                console.error("Error deleting review: " + error);
            })
            .finally(() => {
                // Membersihkan semua modals
                deleteReviewConfirmationModal.hide();
                unauthorizedDeleteModal.hide();
            });
        };
    } else if (userType === "X") {
        const guestWarningModal = new bootstrap.Modal(document.getElementById('guestWarningModal'));
        guestWarningModal.show();
    }
}

// Function to update the data count asynchronously
async function updateDataCount() {
    const response = await fetch(`data_count/${book_id}/`);
    if (response.ok) {
        const dataCount = await response.text();
        document.getElementById("data_count").textContent = dataCount;
    }
}

// Call the updateDataCount function when the page loads
document.addEventListener("DOMContentLoaded", function () {
    updateDataCount();
});

// Panggil refreshReview saat halaman dimuat
refreshReview();

document.addEventListener("DOMContentLoaded", function () {
    var myModal = new bootstrap.Modal(document.getElementById('exampleModal'));
});
