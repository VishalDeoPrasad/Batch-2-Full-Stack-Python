let student = {
    'f_name':'Vishal',
    'l_name':'Kumar',
    'age': 30,
    'marks': 98,
    'full_name': function(){
        return this.f_name + " " + this.l_name;
    }
};

console.log(student.full_name());