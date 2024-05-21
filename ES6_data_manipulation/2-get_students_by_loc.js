export default function getStudentsByLocation(students, city) {
  if (!Array.isArray(students)) {
    return [];
  }

  const rslt = students.filter((item) => item.location === city);

  return rslt;
}
