export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  get name() { return this._name; }

  set name(nvalue) {
    if (typeof nvalue !== 'string') throw new TypeError('Name must be a string');
    this._name = nvalue;
  }

  get length() { return this._length; }

  set length(lvalue) {
    if (!Number.isInteger(lvalue)) throw new TypeError('Length must be a number');
    this._length = lvalue;
  }

  get students() { return this._students; }

  set students(svalue) {
    if (!Array.isArray(svalue)) throw new TypeError('Students must be an array of strings');
    this._students = svalue;
  }
}
