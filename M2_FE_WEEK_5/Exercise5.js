const student = {
	name: "John Doe",
	grades: [
		{name: "math",grade: 80},
		{name: "science",grade: 100},
		{name: "history",grade: 60},
		{name: "PE",grade: 90},
		{name: "music",grade: 98}
	]
}

function resumeStudent (student) {

    const result = {};
    let average = 0;
    let highestNote = 0;
    let lowestNote = 100;

    for (const course of student.grades){
        average += course.grade;

        if (course.grade > highestNote){
            highestNote = course.grade;
            highestClass = course.name;
        };

        if (course.grade < lowestNote){
            lowestNote = course.grade;
            lowestClass = course.name;
        };
    }

    result.name = student.name;
    result.gradeAvg = average/student.grades.length;
    result.highestGrade = highestClass;
    result.lowestGrade = lowestClass;
    
    return result;
}

console.log (resumeStudent(student));