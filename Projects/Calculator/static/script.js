// =========================================================
// SELECT DOM ELEMENTS
// =========================================================
const expressionDisplay = document.getElementById("expression");
const resultDisplay = document.getElementById("result");
const historyList = document.getElementById("history-list");
const buttons = document.querySelectorAll(".btn");

// =========================================================
// CALCULATOR STATE
// =========================================================
let num1 = "";
let num2 = "";
let operator = "";
let isEnteringNum2 = false;

// =========================================================
// UPDATE DISPLAY
// =========================================================
function updateDisplay(value) {
    resultDisplay.textContent = value;
}

function updateExpression() {
    expressionDisplay.textContent = `${num1} ${operator} ${num2}`;
}

// =========================================================
// HANDLE NUMBER INPUT
// =========================================================
function handleNumber(value) {

    // Prevent multiple decimal points
    if (value === "." && !isEnteringNum2 && num1.includes(".")) return;
    if (value === "." && isEnteringNum2 && num2.includes(".")) return;

    if (!isEnteringNum2) {
        num1 += value;
        updateDisplay(num1);
    } else {
        num2 += value;
        updateDisplay(num2);
    }
    updateExpression();
}

// =========================================================
// HANDLE OPERATOR INPUT
// =========================================================
function handleOperator(value) {
    if (num1 === "") return;
    operator = value;
    isEnteringNum2 = true;
    updateExpression();
}

// =========================================================
// HANDLE CLEAR
// =========================================================
function handleClear() {
    num1 = "";
    num2 = "";
    operator = "";
    isEnteringNum2 = false;
    updateDisplay("0");
    expressionDisplay.textContent = "";
}

// =========================================================
// HANDLE TOGGLE SIGN
// =========================================================
function handleToggleSign() {
    if (!isEnteringNum2 && num1 !== "") {
        num1 = String(parseFloat(num1) * -1);
        updateDisplay(num1);
    } else if (isEnteringNum2 && num2 !== "") {
        num2 = String(parseFloat(num2) * -1);
        updateDisplay(num2);
    }
    updateExpression();
}

// =========================================================
// SEND TO FLASK & GET RESULT
// =========================================================
async function handleCalculate() {
    if (num1 === "" || num2 === "" || operator === "") return;

    try {
        const response = await fetch("/calculate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                num1: parseFloat(num1),
                num2: parseFloat(num2),
                operation: operator
            })
        });

        const data = await response.json();

        if (data.error) {
            updateDisplay(data.error);
        } else {
            updateDisplay(data.result);
            expressionDisplay.textContent = `${num1} ${operator} ${num2} =`;
            updateHistory(data.history);

            // Result becomes num1 for chaining calculations
            num1 = String(data.result);
            num2 = "";
            operator = "";
            isEnteringNum2 = false;
        }

    } catch (error) {
        updateDisplay("Error");
        console.error("Calculation error:", error);
    }
}

// =========================================================
// UPDATE HISTORY PANEL
// =========================================================
function updateHistory(historyData) {
    historyList.innerHTML = "";
    historyData.slice().reverse().forEach(entry => {
        const li = document.createElement("li");
        li.classList.add("history__item");
        li.textContent = entry;
        historyList.appendChild(li);
    });
}

// =========================================================
// HANDLE ALL BUTTON CLICKS
// =========================================================
buttons.forEach(button => {
    button.addEventListener("click", () => {
        const action = button.dataset.action;
        const value = button.dataset.value;

        if (action === "clear") handleClear();
        else if (action === "toggle-sign") handleToggleSign();
        else if (action === "calculate") handleCalculate();
        else if (button.classList.contains("btn--operator")) handleOperator(value);
        else if (button.classList.contains("btn--number")) handleNumber(value);
    });
});