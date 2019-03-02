//封装一个代替getElementById()的方法
function byId(id) {
    return typeof(id) === "string"?document.getElementById(id):id;
}

//全局变量
var index = 0,
    timer = null,//间歇调用的方法变量
    //pics是一个数组，从banneer处获得的3个div是其元素，可以用索引的方法获取出来
    pics = byId("banner").getElementsByTagName("div"),
    dots = byId("dots").getElementsByTagName("span"),
    prev = byId('button prev'),
    next = byId('button next'),
    len = pics.length,//pics中div的数量
    menu = byId("menu-content"),
    item = menu.getElementsByClassName("menu-item"),
    subMenu = byId("sub-menu"),
    innerBox = subMenu.getElementsByClassName("inner-box"),//innerBox是一个数组
    itemFont = byId("item-font");


function slideImg() {
    var main = byId("main");
    //滑过清除定时器，离开继续
    main.onmouseover = function () {
        if(timer) clearInterval(timer);//鼠标滑过清除间歇调用
    };
    main.onmouseout = function () {
        timer = setInterval(function () {
            index++;//index自动赋值；index将会在changeImg()中用到
            if(index>=len){
                index = 0;
            }
            changeImg();
        },2000);
    }

    //主动激活onmouseout()方法，让图片自动轮播
    main.onmouseout();

    //点击圆点切换图片
    for (var d=0;d<len;d++) {
        //给所有的span属性添加一个id的属性，值为d，作为当前span的索引
        dots[d].id = d;
        dots[d].onclick = function () { //给所有圆点绑定一个点击事件
            index = this.id;//通过点击给index赋值，将id的值赋给index
            this.className = "active";
            changeImg();
        }
    }

    //点击按钮切换图片
    next.onclick = function () {
        index++;
        if (index>=len) index=0;
        changeImg();
    }
    prev.onclick = function () {
        index--;
        if (index<0) index=2;
        changeImg();
    }

    //导航菜单
    for(var m=0;m<item.length;m++){
        //给每一个menu-item定义data-index属性，作为索引
        item[m].setAttribute("data-index",m);
        //鼠标滑过时显示子菜单
        item[m].onmouseover = function () {
            subMenu.className = "sub-menu";
            var idx = this.getAttribute("data-index");//将自定义属性data-index赋值给idx，idx作为索引
            //将所有子菜单隐藏起来；将背景隐藏起来  功能：清除添加的效果
            for (var j=0;j<innerBox.length;j++){
                innerBox[j].style.display = 'none'; //先将所有子菜单隐藏起来，以便后面根据索引显示指定子菜单
                item[j].style.background = 'none'; //先将所有背景隐藏起来，以便后面根据索引显示背景
            }
            item[idx].style.background = 'rgba(0,0,0,0.1)';
            innerBox[idx].style.display = 'block';

        }
        //鼠标离开后关闭子菜单
        menu.onmouseout = function () {
            subMenu.className = "sub-menu hide";
        }
        //鼠标滑到子菜单时显示子菜单
        subMenu.onmouseover = function () {
            subMenu.className = "sub-menu";
        }
        //鼠标离开子菜单时关闭子菜单
        subMenu.onmouseout = function () {
            subMenu.className = "sub-menu hide";
        }

    }


}



//切换图片；根据索引显现出来
function changeImg() {
    //因为for循环下面的代码块会添加'block'代码和’active‘的类，所以需要遍历banner所有div将其隐藏起来
    for (var i=0;i<len;i++){
        pics[i].style.display = 'none';
        dots[i].className = '';
    }
    pics[index].style.display = 'block';//利用index作为索引取出控制轮播图片div；然后让其显示出来
    dots[index].className = "active";//利用index作为索引取出span，然后给其添加active的类
}



slideImg();