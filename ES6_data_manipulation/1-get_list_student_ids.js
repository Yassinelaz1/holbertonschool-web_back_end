export default function getListStudentIds(students) {
  if (!Array.isArray(students)) {
    return [];
  }

  const studentid = students.map((item) => item.id);

  return studentid;
}
