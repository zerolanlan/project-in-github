package 考试;
import java.util.InputMismatchException;
import java.util.Scanner;

public class 选课系统 {

    public static void main(String[] args) {
        //Init The Class
    
        Scanner console=new Scanner(System.in);


        int num;
        int id;
        String name;
        while(1==1) {
            System.out.println("欢迎来到选课系统");
            System.out.println("请输入你的学号");
            num=console.nextInt();
            id=num;
            if (num == 99991111) {
                System.out.println("你好，管理员，请输入管理员密码");
                num=console.nextInt();
                int flag=0;
                while(num!=1120172954){
                    System.out.println("管理员密码错误，请重新输入<输入56879退出管理员模式>");
                    num=console.nextInt();
                    if(num==56879) {
                        flag=1;
                        break;
                    }
                }
                if (flag==1) continue;

                //************************************管理员模式代码*****************************************
                System.out.println("你好，管理员！请输入要执行的操作代码");
                while(1==1) {
                    System.out.println("查看课程");
                    System.out.println("添加课程");
                    System.out.println("查看所有学生及选课信息");
                    System.out.println("退出管理员模式");
                    int tmp;
                    tmp=console.nextInt();
                    while (tmp<=0 || tmp>=5) {
                        System.out.println("代码错误，请输入1到4之间的代码");
                    }
                    if (tmp == 4) break;
                    if (tmp == 1) {
                        course.PrintCourseList();
                        System.out.println("**********************分割线***********************");
                        continue;
                    }
                    String TmpName;
                    if (tmp == 2) {
                        System.out.println("请输入要添加的课程，系统将自动分配代号");
                        TmpName=console.next();
                        if (course.CourseExist(TmpName)==true) {
                            System.out.println("课程已经存在");
                            continue;
                        }
                        Course course=new Course(TmpName);
                        course.AddCourse(course);
                        System.out.println("添加课程成功，课程代码"+course.ID+"  课程名称："+course.name);
                        System.out.println("**********************分割线***********************");
                        continue;
                    }
                    if (tmp == 3) {
                        e.PrintSCInfo();
                        System.out.println("**********************分割线***********************");
                        continue;
                    }
                }
                continue;
            }


            name=e.StudentExist(num);
            if (name!="111111") {
                System.out.println("你好，"+name);
            }
            else {
                System.out.println("请输入你的姓名");
                name=console.next();
                System.out.println("你好，"+name+",你的学号是"+num+"。信息添加成功");
               
            }
            while(1==1){
                System.out.println("请选择操作并输入操作代号");
                System.out.println("1 查看已选课程");
                System.out.println("2 选课");
                System.out.println("3 删除课程");
                System.out.println("4 退出");
                System.out.println("**********************分割线***********************");
                num=console.nextInt();
                if (num<=0 || num>=5)
                do {
                    System.out.println("请输入1到3之间的整数");
                    num=console.nextInt();
                }while(num<=0 || num >4);
                if(num==4) break;
                if (num == 1) {
                    e.PrintSingleStudentInfo(id);
                    System.out.println("**********************分割线***********************");
                    continue;
                }
                else if (num == 2) {
                    course.PrintCourseList();
                    while(1==1){
                        System.out.println("请输入要选的课程代码,输入9999退出");
                        int CID=console.nextInt();
                        if(CID==9999) break;
                        if (course.CourseExist(CID)==false) {
                            System.out.println("课程不存在");
                            System.out.println("**********************分割线***********************");
                            continue;
                        }
                        if (e.StudentCourseExist(CID)==true) {
                            System.out.println("你已经选择了该课程");
                            System.out.println("**********************分割线***********************");
                            continue;
                        }
                        Course course=new Course();
                        course.ID=CID;
                        course.name=course.ReturnCourseName(CID);
                        e.AddCourse(course);
                        System.out.println("你已经成功选择了该课程:"+CID+" "+course.name);
                        System.out.println("**********************分割线***********************");
                    }
                }
                else if (num == 3) {
                    System.out.println("你的已选课程列表为");
                    e.PrintSingleStudentInfo(id);
                    while(1==1) {
                        System.out.println("请输入要删除的课程代码，输入9999退出");
                        int CID=console.nextInt();
                        if (CID==9999) break;
                        if (course.CourseExist(CID)==false) {
                            System.out.println("课程不存在");
                            System.out.println("**********************分割线***********************");
                            continue;
                        }
                        if (e.StudentCourseExist(CID)==false) {
                            System.out.println("你并未选择了该课程");
                            System.out.println("**********************分割线***********************");
                            continue;
                        }
                        e.CourseDelete(CID);    
                        System.out.println("你成功的删除了课程"+CID+" "+course.ReturnCourseName(CID));
                        System.out.println("**********************分割线***********************");
                    }
                }
            }   
        }   
        }   
}
