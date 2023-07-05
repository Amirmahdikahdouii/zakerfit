jalaliDatepicker.startWatch();
let changeBirthdayButton = document.getElementById("change-birthday-button");
let changeGenderTypeButton = document.getElementById("change-gender-type-button");
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