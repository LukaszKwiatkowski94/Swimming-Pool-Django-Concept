const nav = document.querySelector(".nav");
const btnNav = document.querySelector(".nav__btn");
const btnNavOpen = document.querySelector(".nav__btn-content");
const navMenu = document.querySelector(".nav__list");

const showNav = () => {
	nav.classList.toggle("nav__hide");
	navMenu.classList.toggle("nav__show-animation");
	btnNavOpen.classList.toggle("nav__btn--exit");
};

btnNav.addEventListener("click", showNav);
