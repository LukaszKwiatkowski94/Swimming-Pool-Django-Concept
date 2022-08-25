const btnBuy = document.querySelector(".transaction__btn");
const errorBuy = document.querySelector(".transaction__disabled");
let idUser = 0;
let idPass = 0;
let urlAfterBuy = "";

window.onload = function () {
	idUser = document.querySelector(".id-user").getAttribute("value");
	idPass = document.querySelector(".id-pass").getAttribute("value");
	urlAfterBuy = document.querySelector(".url-after-buy").getAttribute("value");
};

const buyPass = () => {
	btnBuy.classList.add("btn--disabled");
	btnBuy.disabled = true;
	const params = {
		user: idUser,
		passId: idPass,
	};
	let options = {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(params),
	};
	fetch("/transactions/transactionPass/", options)
		.then((response) => response.json())
		.then((data) => {
			if (data == "success") {
				document.location.href = urlAfterBuy;
			} else {
				errorBuy.textContent = data;
			}
		});
};

btnBuy.addEventListener("click", buyPass);
