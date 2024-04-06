const calorieCounter = document.getElementById('calorie-counter');
const budgetNumberInput = document.getElementById('budget');
const entryDropdown = document.getElementById('entry-dropdown');
const addEntryButton = document.getElementById('add-entry');
const clearButton = document.getElementById('clear');
const output = document.getElementById('output');
let isError = false;

function cleanInputString(str) {
    // The split() method splits a string into an array of substrings, and returns the new array.
    // const strArray = str.split('');
    const regex = /[+-\s]/g; // g - global search,  continue looking after it has found a match.
    //replace() allows you to replace characters in the string with another string. .replace takes two arguments.
    // The first argument is the character you want to replace, and the second argument is the character you want to replace it with.
    return str.replace(regex, '');
}

function isInvalidInput(str) {
    const regex = /\d+e\d+/i; // i - case-insensitive search, /d - digit
    //The + modifier in a regex allows you to match a pattern that occurs one or more times
    return str.match(regex);
}

function addEntry() {
    // template literals are enclosed by the back-tick (` `) (grave accent) character instead of double or single quotes.
    // template literals can contain placeholders. These are indicated by the dollar sign and curly braces (${expression}).
    const targetInputContainer = document.querySelector(`#${entryDropdown.value} .input-container`);
    // The querySelectorAll() method returns a NodeList of all the elements that match the selector.
    const entryNumber = targetInputContainer.querySelectorAll('input[type="text"]').length + 1;
    const HTMLString = `
        <label for="${entryDropdown.value}-${entryNumber}-name">Entry ${entryNumber} Name</label>
        <input type="text" id="${entryDropdown.value}-${entryNumber}-name" placeholder="Name" />
        <label for="${entryDropdown.value}-${entryNumber}-calories">Entry ${entryNumber} Calories</label>
        <input type="number" min="0" id="${entryDropdown.value}-${entryNumber}-calories" placeholder="Calories" />`;
    // The insertAdjacentHtml method takes two arguments. The first argument is a string that specifies the position of the new element.
    // The second argument is the HTML content you want to insert.
    targetInputContainer.insertAdjacentHTML("beforeend", HTMLString);
}

function calculateCalories(e) {
    e.preventDefault();
    isError = false;
    const breakfastNumberInputs = document.querySelectorAll('#breakfast input[type=number]');
    const lunchNumberInputs = document.querySelectorAll('#lunch input[type=number]');
    const dinnerNumberInputs = document.querySelectorAll('#dinner input[type=number]');
    const snacksNumberInputs = document.querySelectorAll('#snacks input[type=number]');
    const exerciseNumberInputs = document.querySelectorAll('#exercise input[type=number]');

    const breakfastCalories = getCaloriesFromInputs(breakfastNumberInputs);
    const lunchCalories = getCaloriesFromInputs(lunchNumberInputs);
    const dinnerCalories = getCaloriesFromInputs(dinnerNumberInputs);
    const snacksCalories = getCaloriesFromInputs(snacksNumberInputs);
    const exerciseCalories = getCaloriesFromInputs(exerciseNumberInputs);
    const budgetCalories = getCaloriesFromInputs([budgetNumberInput]);
    if (isError) {
        return;
    }
    const consumedCalories = breakfastCalories + lunchCalories + dinnerCalories + snacksCalories;
    const remainingCalories = budgetCalories - consumedCalories + exerciseCalories;
    const surplusOrDeficit = remainingCalories < 0 ? 'Surplus' : 'Deficit';
    output.innerHTML = ``;
}

function getCaloriesFromInputs(list) {
    let calories = 0;
    for (const item of list) {
        const currVal = cleanInputString(item.value);
        const invalidInputMatch = isInvalidInput(currVal);

        if (invalidInputMatch) {
            alert(`Invalid Input: ${invalidInputMatch[0]}`);
            isError = true;
            return null;
        }
        // Number constructor is a function that converts a value to a number.
        calories += Number(currVal);
    }
    return calories;
}

addEntryButton.addEventListener('click', addEntry);