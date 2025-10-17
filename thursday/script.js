async function fetchStudents() {
  const container = document.getElementById("students-container");
  const errorMsg = document.getElementById("error");

  try {
    // Load API URL from config.json
    const configResponse = await fetch("./config.json");
    if (!configResponse.ok) throw new Error("Failed to load config.json");

    const config = await configResponse.json();
    const apiUrl = config.apiUrl;

    // Fetch student data
    const response = await fetch(apiUrl);
    if (!response.ok) throw new Error("Failed to fetch student data");

    const data = await response.json();
    const students = data["Students Details"];

    // Display students
    container.innerHTML = students.map(student => `
      <div class="card">
        <h3>${student.Name}</h3>
        <p><strong>Age:</strong> ${student.Age}</p>
        <p><strong>Sex:</strong> ${student.Sex}</p>
        <p><strong>City:</strong> ${student.City}</p>
        <p><strong>Track:</strong> ${student.Track}</p>
      </div>
    `).join("");

    errorMsg.textContent = "";
  } catch (error) {
    console.error("Error:", error);
    errorMsg.textContent = "❌ Failed to load data. Check config.json or server.";
  }
}

fetchStudents();
