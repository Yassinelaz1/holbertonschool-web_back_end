export default function createInt8TypedArray(length, position, value) {
  const array = new ArrayBuffer(length);
  const buffer = new DataView(array, 0);
  if (position > length - 1) {
    throw Error('Position outside range');
  }
  buffer.setInt8(position, value);
  return buffer;
}
