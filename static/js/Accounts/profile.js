jalaliDatepicker.startWatch();
let changeBirthdayButton = document.getElementById("change-birthday-button");
let changeGenderTypeButton = document.getElementById("change-gender-type-button");
let changeImageButton = document.getElementById("change-image-button");
let submitChangeImageButton = document.getElementById("submit-change-image-button");
let changeImageInput = document.getElementById("change-image-input");

changeBirthdayButton.addEventListener("change", () => {
    let url = `/Accounts/change-user-birthday/`;
    let data = {
        "date": changeBirthdayButton.value,
    }
    let options = {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
    }
    fetch(url, options).then(({status}) => {
        if (status === 200) {
            Swal.fire({
                icon: "success",
                title: "پیغام",
                text: "تاریخ تولد با موفقیت تغییر کرد",
                timer: 3000,
                showConfirmButton: false
            })
        }
    })
})
changeGenderTypeButton.addEventListener("click", () => {
    let url = `/Accounts/change-user-gender/`;
    fetch(url, {method: "POST"})
        .then(response => response.json())
        .then((data) => {
            Swal.fire({
                icon: "success",
                title: "پیغام",
                text: "جنسیت با موفقیت تغییر کرد",
                timer: 3000,
                showConfirmButton: false
            })
            let userGenderType = document.getElementById("user-gender-type");
            if (data.gender === 1) {
                userGenderType.innerText = `آقا`;
            } else {
                userGenderType.innerText = `خانم`;
            }
        })
})

changeImageButton.addEventListener("click", () => {
    changeImageInput.click();
    changeImageButton.classList.add("d-none");
    submitChangeImageButton.classList.remove("d-none")
});
submitChangeImageButton.addEventListener("click", (e) => {
    const uploadAgainWorks = (alertText) => {
        e.preventDefault();
        changeImageButton.classList.remove("d-none");
        submitChangeImageButton.classList.add("d-none");
        changeImageInput.value = '';
        changeImageInput.type = '';
        changeImageInput.type = 'file';
        Swal.fire({
            icon: "warning",
            title: "هشدار!",
            text: alertText,
            timer: 3000,
            showConfirmButton: false,
            position: "center",
        })
    }
    if (changeImageInput.files.length !== 1) {
        uploadAgainWorks("عکسی انتخاب نشده است");
        return null;
    } else if (changeImageInput.files.length > 1) {
        uploadAgainWorks("لطفا فقط یک فایل انتخاب کنید");
        return null;
    }
    file = changeImageInput.files[0];
    if (!file.type.startsWith("image/")) {
        uploadAgainWorks("لطفا فقط عکس انتخاب کنید.");
        return null;
    }
})