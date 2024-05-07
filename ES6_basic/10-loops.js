export default function appendToEachArrayValue(array, appendString) {
  const i = [];
  for (const value of array) {
    i.push(appendString + value);
  }

  return i;
}
