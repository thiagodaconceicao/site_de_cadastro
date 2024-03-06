//import { GetUser } from "./postgres.js";

document.getElementById('registrationForm').addEventListener('submit', async (event) => {
  event.preventDefault(); // Prevent the form from submitting normally

  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  try {
    const result = await GetUser(email, password);
    console.log("User added:", result);
    // Do something with the result, maybe redirect the user or display a success message
  } catch (error) {
    console.error("Error adding user:", error);
    // Handle the error, maybe display an error message to the user
  }
});
