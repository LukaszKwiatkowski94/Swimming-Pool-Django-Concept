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

const setClick = () => {
	const users = document.querySelectorAll(".users__name");
	users.forEach((item) => {
		item.addEventListener("click", () => {
			let box = item.parentElement;
			let nameRadio = item.getAttribute("data-name");
			box.innerHTML = "";
			box.append(item, getUserOption(nameRadio));
		});
	});
};

const getUsersByEmail = (userEmail) => {
	const params = {
		email: userEmail,
	};
	let options = {
		method: "POST",
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify(params),
	};
	fetch("/user/getUsersList/", options)
		.then((response) => response.json())
		.then((data) => {
			console.log(data);
		});
};

setClick();
getUsersByEmail('user@test.com');
