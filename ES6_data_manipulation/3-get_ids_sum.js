export default function getStudentIdsSum(students) {
  if (!Array.isArray(students)) {
    return [];
  }
  const reducer = (total, student) => total + student.id;
  const sum = students.reduce(reducer, 0);
  return sum;
}
