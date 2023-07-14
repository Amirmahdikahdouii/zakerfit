let numberInputes = [...document.getElementsByClassName('digit-input')];
let submitButton = document.getElementById("submit-button");
let form = document.getElementById("form");

numberInputes.forEach((element, index) => {
    element.addEventListener("input", () => {
        if (index + 1 !== numberInputes.length) {
            numberInputes[index + 1].focus();
        }
    })
})

submitButton.addEventListener("click", (e) => {
    let value = "";
    numberInputes.forEach(element => {
        value += element.value;
    })
    let alertOptions = {
        icon: "error",
        title: "خطا",
        text: "لطفا کد را به درستی وارد کنید.",
        showConfirmButton: false,
        timer: 3000,
        toast: true,
        position: 'center',
    }
    if (value.length < 6) {
        Swal.fire(alertOptions);
    } else if (value.length > 6) {
        alertOptions['text'] = "لطفا کد 6 رقمی وارذ کنید";
        Swal.fire(alertOptions);
    } else {
        let options = {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({"code": value,}),
        }
        fetch(`${form.action}`, options).then(({status}) => {
            if (status === 200) {
                Swal.fire({
                    icon: 'success',
                    title: 'پیغام',
                    text: "کد با موفقیت تایید شد",
                    showConfirmButton: false,
                    timer: 3000,
                });
                setTimeout(() => {
                    location.replace("/Accounts/profile");
                }, 3000)
            } else {
                Swal.fire({
                    icon: 'error',
                    title: 'خطا',
                    text: "کد نادرست است",
                    showConfirmButton: false,
                    timer: 3000,
                });
                numberInputes.forEach(element => {
                    element.value = "";
                })
            }
        })
    }
})