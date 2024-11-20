const { add, subtract, multiply, divide } = require('./calc');

test('adds 5 + 3 to equal 8', () => {
  expect(add(5, 3)).toBe(8);
});

test('subtracts 5 - 3 to equal 2', () => {
  expect(subtract(5, 3)).toBe(2);
});

test('multiplies 5 * 3 to equal 15', () => {
  expect(multiply(5, 3)).toBe(15);
});

test('divides 6 / 3 to equal 2', () => {
  expect(divide(6, 3)).toBe(2);
});

test('divides 5 / 0 to return error message', () => {
  expect(divide(5, 0)).toBe("Error: Division by zero");
});