const listBtnPass = document.querySelectorAll(".btn-pass");

const transactionPass = (idPass) => {
	var url = `transactions/buyPass/${idPass}/`;
	document.location.href = '../' + url;
};

listBtnPass.forEach((element) => {
	element.addEventListener("click", () =>
		transactionPass(element.getAttribute("data-idPass"))
	);
});
