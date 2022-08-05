const inputEmail = document.querySelector(".input-user-email");

const getUserOption = (nameRadio) => {
	let name = nameRadio;
	const ruleList = {
		1: "Client",
		2: "Administrator",
		3: "Cashier",
		4: "Customer service",
		5: "Accountant",
		6: "Press spokesman",
		7: "Management",
	};
	const rule = (value, content) => {
		let label = document.createElement("label");
		label.classList.add("input-box__label");
		label.setAttribute("for", content.replace(" ", "_") + "_" + name);
		let input = document.createElement("input");
		input.setAttribute("type", "radio");
		input.setAttribute("name", name);
		input.setAttribute("id", content.replace(" ", "_") + "_" + name);
		input.setAttribute("value", value);
		label.append(input, content);
		return label;
	};
	const optionsList = document.createElement("div");
	optionsList.classList.add("users__option");
	for (let key in ruleList) {
		let value = ruleList[key];
		optionsList.append(rule(key, value));
	}
	return optionsList;
};

const setClick = (item) => {
	let box = item.parentElement;
	let nameRadio = item.getAttribute("data-name");
	box.innerHTML = "";
	box.append(item, getUserOption(nameRadio));
};

const createUsersHeader = (data) => {
	let itemsOfUsers = document.querySelector(".set-rule__users");
	data.forEach((user) => {
		let itemU = document.createElement("div");
		itemU.classList.add("users__item");
		let nameU = document.createElement("div");
		nameU.classList.add("users__name");
		nameU.setAttribute("data-name", user.fields.email);
		let p = document.createElement("p");
		p.textContent = `${user.fields.email} - ${user.fields.nameUser} ${user.fields.surnameUser}`;
		nameU.append(p);
		nameU.addEventListener("click", (nameU) => setClick(nameU.target));
		itemU.append(nameU);
		itemsOfUsers.append(itemU);
	});
};

const getUsersByEmail = (userEmail) => {
	const params = {
		email: userEmail,
	};
	let options = {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(params),
	};
	fetch("/user/getUsersList/", options)
		.then((response) => response.json())
		.then((data) => {
			createUsersHeader(data);
		});
};

function inputHandler(e) {
	if (e.key == "Enter" || inputEmail.value.length > 4) {
		getUsersByEmail(inputEmail.value);
	}
}

inputEmail.addEventListener("keyup", (e) => inputHandler(e));
