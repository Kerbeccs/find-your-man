const studentLoginBtn = document.getElementById("student-login-btn");
const teacherLoginBtn = document.getElementById("teacher-login-btn");
const loginForm = document.getElementById("login-form");

studentLoginBtn.addEventListener("click", () => {
  
  loginForm.action = "{% url 'student:login' %}";
});

teacherLoginBtn.addEventListener("click", () => {
 
  loginForm.action = "{% url 'teacher:login' %}";
});

function showContainer() {
  const container = document.querySelector('.container');
  container.classList.add('show');
}

setTimeout(showContainer, 1000);
