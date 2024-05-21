export default function getStudentsByLocation(array, city, grad) {
  return array
    .filter((i) => i.location === city)
    .map((student) => {
      const gradeFilter = grade
        .filter((i) => i.id === student.id)
        .map((x) => x.grade)[0];
      const grade = gradeFilter || 'N/A';
      return { ...student, grade };
    });
}
