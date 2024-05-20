export default function getListStudentIds(students) {
  if (!Array.isArray(students)) {
    return [];
  }

  const student_id = students.map((item) => item.id);

  return student_id;
}
