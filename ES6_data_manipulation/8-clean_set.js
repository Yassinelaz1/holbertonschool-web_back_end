export default function cleanSet(set, startString) {
  const str = [];
  const rslt = '';

  if (typeof set !== 'object' || typeof startString !== 'string' || startString.length === 0) {
    return rslt;
  }

  for (const item of set) {
    if (item && item.startsWith(startString)) {
      str.push(item.slice(startString.length));
    }
  }
  return str.join('-');
}
