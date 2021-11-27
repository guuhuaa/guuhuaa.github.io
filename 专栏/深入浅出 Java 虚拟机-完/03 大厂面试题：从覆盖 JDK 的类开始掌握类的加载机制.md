<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>03 大厂面试题：从覆盖 JDK 的类开始掌握类的加载机制.md</title>
        <!-- Spectre.css framework -->
        <link rel="stylesheet" href="../../static/index.css">
        <!-- theme css & js -->
        <meta name="generator" content="Hexo 4.2.0">
    </head>

<body>

<div class="book-container">
    <div class="book-sidebar">
        <div class="book-brand">
            <a href="../../index.html">
                <img src="../../static/favicon.png">
                <span>技术文章摘抄</span>
            </a>
        </div>
        <div class="book-menu uncollapsible">
            <ul class="uncollapsible">
                <li><a href="../../index.html" class="current-tab">首页</a></li>
            </ul>

            <ul class="uncollapsible">
                <li><a href="../index.html">上一级</a></li>
            </ul>

            <ul class="uncollapsible">
                <li>

                    
                    <a href="00&#32;开篇词：JVM，一块难啃的骨头.md">00 开篇词：JVM，一块难啃的骨头.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;一探究竟：为什么需要&#32;JVM？它处在什么位置？.md">01 一探究竟：为什么需要 JVM？它处在什么位置？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;大厂面试题：你不得不掌握的&#32;JVM&#32;内存管理.md">02 大厂面试题：你不得不掌握的 JVM 内存管理.md</a>

                </li>
                <li>

                    <a class="current-tab" href="03&#32;大厂面试题：从覆盖&#32;JDK&#32;的类开始掌握类的加载机制.md">03 大厂面试题：从覆盖 JDK 的类开始掌握类的加载机制.md</a>
                    

                </li>
                <li>

                    
                    <a href="04&#32;动手实践：从栈帧看字节码是如何在&#32;JVM&#32;中进行流转的.md">04 动手实践：从栈帧看字节码是如何在 JVM 中进行流转的.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;大厂面试题：得心应手应对&#32;OOM&#32;的疑难杂症.md">05 大厂面试题：得心应手应对 OOM 的疑难杂症.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;深入剖析：垃圾回收你真的了解吗？（上）.md">06 深入剖析：垃圾回收你真的了解吗？（上）.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;深入剖析：垃圾回收你真的了解吗？（下）.md">07 深入剖析：垃圾回收你真的了解吗？（下）.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;大厂面试题：有了&#32;G1&#32;还需要其他垃圾回收器吗？.md">08 大厂面试题：有了 G1 还需要其他垃圾回收器吗？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;案例实战：亿级流量高并发下如何进行估算和调优.md">09 案例实战：亿级流量高并发下如何进行估算和调优.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;第09讲：案例实战：面对突如其来的&#32;GC&#32;问题如何下手解决.md">10 第09讲：案例实战：面对突如其来的 GC 问题如何下手解决.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;第10讲：动手实践：自己模拟&#32;JVM&#32;内存溢出场景.md">11 第10讲：动手实践：自己模拟 JVM 内存溢出场景.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;第11讲：动手实践：遇到问题不要慌，轻松搞定内存泄漏.md">12 第11讲：动手实践：遇到问题不要慌，轻松搞定内存泄漏.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;工具进阶：如何利用&#32;MAT&#32;找到问题发生的根本原因.md">13 工具进阶：如何利用 MAT 找到问题发生的根本原因.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;动手实践：让面试官刮目相看的堆外内存排查.md">14 动手实践：让面试官刮目相看的堆外内存排查.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;预警与解决：深入浅出&#32;GC&#32;监控与调优.md">15 预警与解决：深入浅出 GC 监控与调优.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;案例分析：一个高死亡率的报表系统的优化之路.md">16 案例分析：一个高死亡率的报表系统的优化之路.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;案例分析：分库分表后，我的应用崩溃了.md">17 案例分析：分库分表后，我的应用崩溃了.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;动手实践：从字节码看方法调用的底层实现.md">18 动手实践：从字节码看方法调用的底层实现.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;大厂面试题：不要搞混&#32;JMM&#32;与&#32;JVM.md">19 大厂面试题：不要搞混 JMM 与 JVM.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;动手实践：从字节码看并发编程的底层实现.md">20 动手实践：从字节码看并发编程的底层实现.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;动手实践：不为人熟知的字节码指令.md">21 动手实践：不为人熟知的字节码指令.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;深入剖析：如何使用&#32;Java&#32;Agent&#32;技术对字节码进行修改.md">22 深入剖析：如何使用 Java Agent 技术对字节码进行修改.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;动手实践：JIT&#32;参数配置如何影响程序运行？.md">23 动手实践：JIT 参数配置如何影响程序运行？.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;案例分析：大型项目如何进行性能瓶颈调优？.md">24 案例分析：大型项目如何进行性能瓶颈调优？.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;未来：JVM&#32;的历史与展望.md">25 未来：JVM 的历史与展望.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;福利：常见&#32;JVM&#32;面试题补充.md">26 福利：常见 JVM 面试题补充.md</a>

                </li>
            </ul>

        </div>
    </div>

    <div class="sidebar-toggle" onclick="sidebar_toggle()" onmouseover="add_inner()" onmouseleave="remove_inner()">
        <div class="sidebar-toggle-inner"></div>
    </div>

    <script>
        function add_inner() {
            let inner = document.querySelector('.sidebar-toggle-inner')
            inner.classList.add('show')
        }

        function remove_inner() {
            let inner = document.querySelector('.sidebar-toggle-inner')
            inner.classList.remove('show')
        }

        function sidebar_toggle() {
            let sidebar_toggle = document.querySelector('.sidebar-toggle')
            let sidebar = document.querySelector('.book-sidebar')
            let content = document.querySelector('.off-canvas-content')
            if (sidebar_toggle.classList.contains('extend')) { // show
                sidebar_toggle.classList.remove('extend')
                sidebar.classList.remove('hide')
                content.classList.remove('extend')
            } else { // hide
                sidebar_toggle.classList.add('extend')
                sidebar.classList.add('hide')
                content.classList.add('extend')
            }
        }
    </script>

    <div class="off-canvas-content">
        <div class="columns">
            <div class="column col-12 col-lg-12">
                <div class="book-navbar">
                    <!-- For Responsive Layout -->
                    <header class="navbar">
                        <section class="navbar-section">
                            <a onclick="open_sidebar()">
                                <i class="icon icon-menu"></i>
                            </a>
                        </section>
                    </header>
                </div>
                <div class="book-content" style="max-width: 960px; margin: 0 auto;
    overflow-x: auto;
    overflow-y: hidden;">
                    <div class="book-post">
                        <p id="tip" align="center"></p>
                        <div><h1>03 大厂面试题：从覆盖 JDK 的类开始掌握类的加载机制</h1>
<p>本课时我们主要从覆盖 JDK 的类开始讲解 JVM 的类加载机制。其实，JVM 的类加载机制和 Java 的类加载机制类似，但 JVM 的类加载过程稍有些复杂。</p>
<p>前面课时我们讲到，JVM 通过加载 .class 文件，能够将其中的字节码解析成操作系统机器码。那这些文件是怎么加载进来的呢？又有哪些约定？接下来我们就详细介绍 JVM 的类加载机制，同时介绍三个实际的应用场景。</p>
<p>我们首先看几个面试题。</p>
<ul>
<li>我们能够通过一定的手段，覆盖 HashMap 类的实现么？</li>
<li>有哪些地方打破了 Java 的类加载机制？</li>
<li>如何加载一个远程的 .class 文件？怎样加密 .class 文件？</li>
</ul>
<p>关于类加载，很多同学都知道双亲委派机制，但这明显不够。面试官可能要你讲出几个能打破这个机制的例子，这个时候不要慌。上面几个问题，是我在接触的一些比较高级的面试场景中，遇到的一些问法。在平常的工作中，也有大量的相关应用，我们会理论联系实践综合分析这些问题。</p>
<h3>类加载过程</h3>
<p>现实中并不是说，我把一个文件修改成 .class 后缀，就能够被 JVM 识别。类的加载过程非常复杂，主要有这几个过程：加载、验证、准备、解析、初始化。这些术语很多地方都出现过，我们不需要死记硬背，而应该要了解它背后的原理和要做的事情。</p>
<p><img src="assets/Cgq2xl4cQNeAO_j6AABZKdVbw1w802.png" alt="img" /></p>
<p>如图所示。<strong>大多数情况下</strong>，类会按照图中给出的顺序进行加载。下面我们就来分别介绍下这个过程。</p>
<h4>加载</h4>
<p>加载的主要作用是将外部的 .class 文件，加载到 Java 的方法区内，你可以回顾一下我们在上一课时讲的内存区域图。加载阶段主要是找到并加载类的二进制数据，比如从 jar 包里或者 war 包里找到它们。</p>
<h4>验证</h4>
<p>肯定不能任何 .class 文件都能加载，那样太不安全了，容易受到恶意代码的攻击。验证阶段在虚拟机整个类加载过程中占了很大一部分，不符合规范的将抛出 java.lang.VerifyError 错误。像一些低版本的 JVM，是无法加载一些高版本的类库的，就是在这个阶段完成的。</p>
<h4>准备</h4>
<p>从这部分开始，将为一些类变量分配内存，并将其初始化为默认值。此时，实例对象还没有分配内存，所以这些动作是在方法区上进行的。</p>
<p>我们顺便看一道面试题。下面两段代码，code-snippet 1 将会输出 0，而 code-snippet 2 将无法通过编译。</p>
<pre><code>code-snippet 1：

     public class A {

         static int a ;

         public static void main(String[] args) {

             System.out.println(a);

         }

     }

 code-snippet 2：

 public class A {

     public static void main(String[] args) {

         int a ;

         System.out.println(a);

     }

 }
</code></pre>
<p>为什么会有这种区别呢？</p>
<p>这是因为局部变量不像类变量那样存在准备阶段。类变量有两次赋初始值的过程，一次在准备阶段，赋予初始值（也可以是指定值）；另外一次在初始化阶段，赋予程序员定义的值。</p>
<p>因此，即使程序员没有为类变量赋值也没有关系，它仍然有一个默认的初始值。但局部变量就不一样了，如果没有给它赋初始值，是不能使用的。</p>
<h4>解析</h4>
<p>解析在类加载中是非常非常重要的一环，是将符号引用替换为直接引用的过程。这句话非常的拗口，其实理解起来也非常的简单。</p>
<p>符号引用是一种定义，可以是任何字面上的含义，而直接引用就是直接指向目标的指针、相对偏移量。</p>
<p>直接引用的对象都存在于内存中，你可以把通讯录里的女友手机号码，类比为符号引用，把面对面和你吃饭的人，类比为直接引用。</p>
<p>解析阶段负责把整个类激活，串成一个可以找到彼此的网，过程不可谓不重要。那这个阶段都做了哪些工作呢？大体可以分为：</p>
<ul>
<li>类或接口的解析</li>
<li>类方法解析</li>
<li>接口方法解析</li>
<li>字段解析</li>
</ul>
<p>我们来看几个经常发生的异常，就与这个阶段有关。</p>
<ul>
<li>java.lang.NoSuchFieldError 根据继承关系从下往上，找不到相关字段时的报错。</li>
<li>java.lang.IllegalAccessError 字段或者方法，访问权限不具备时的错误。</li>
<li>java.lang.NoSuchMethodError 找不到相关方法时的错误。</li>
</ul>
<p>解析过程保证了相互引用的完整性，把继承与组合推进到运行时。</p>
<h4>初始化</h4>
<p>如果前面的流程一切顺利的话，接下来该初始化成员变量了，到了这一步，才真正开始执行一些字节码。</p>
<p>接下来是另一道面试题，你可以猜想一下，下面的代码，会输出什么？</p>
<pre><code>public class A {

     static int a = 0 ;

     static {

         a = 1;

         b = 1;

     }

     static int b = 0;
     public static void main(String[] args) {

         System.out.println(a);

         System.out.println(b);

     }

 }
</code></pre>
<p>结果是 1 0。a 和 b 唯一的区别就是它们的 static 代码块的位置。</p>
<p>这就引出一个规则：static 语句块，只能访问到定义在 static 语句块之前的变量。所以下面的代码是无法通过编译的。</p>
<pre><code>static {

         b = b + 1;

 }

 static int b = 0;
</code></pre>
<p>我们再来看第二个规则：JVM 会保证在子类的初始化方法执行之前，父类的初始化方法已经执行完毕。</p>
<p>所以，JVM 第一个被执行的类初始化方法一定是 java.lang.Object。另外，也意味着父类中定义的 static 语句块要优先于子类的。</p>
<h4><clinit>与<init></h4>
<p>说到这里，不得不再说一个面试题：<clinit> 方法和 <init> 方法有什么区别？</p>
<p>主要是为了让你弄明白类的初始化和对象的初始化之间的差别。</p>
<pre><code>public class A {

     static {

         System.out.println(&quot;1&quot;);

     }

     public A(){

         System.out.println(&quot;2&quot;);

         }

     }
     public class B extends A {

         static{

         System.out.println(&quot;a&quot;);

     }

     public B(){

         System.out.println(&quot;b&quot;);

     }
     public static void main(String[] args){

         A ab = new B();

         ab = new B();

     }

 }
</code></pre>
<p>先公布下答案：</p>
<pre><code>1

a

2

b

2

b
</code></pre>
<p>你可以看下这张图。其中 static 字段和 static 代码块，是属于类的，在类的加载的初始化阶段就已经被执行。类信息会被存放在方法区，在同一个类加载器下，这些信息有一份就够了，所以上面的 static 代码块只会执行一次，它对应的是 <clinit> 方法。</p>
<p>而对象初始化就不一样了。通常，我们在 new 一个新对象的时候，都会调用它的构造方法，就是 <init>，用来初始化对象的属性。每次新建对象的时候，都会执行。</p>
<p><img src="assets/CgqCHl9ZjveAemjoAAB4J1dCVDo17.jpeg" alt="Lark20200910-102602.jpeg" /></p>
<p>所以，上面代码的 static 代码块只会执行一次，对象的构造方法执行两次。再加上继承关系的先后原则，不难分析出正确结果。</p>
<h3>类加载器</h3>
<p>整个类加载过程任务非常繁重，虽然这活儿很累，但总得有人干。类加载器做的就是上面 5 个步骤的事。</p>
<p>如果你在项目代码里，写一个 java.lang 的包，然后改写 String 类的一些行为，编译后，发现并不能生效。JRE 的类当然不能轻易被覆盖，否则会被别有用心的人利用，这就太危险了。</p>
<p>那类加载器是如何保证这个过程的安全性呢？其实，它是有着严格的等级制度的。</p>
<h4>几个类加载器</h4>
<p>首先，我们介绍几个不同等级的类加载器。</p>
<ul>
<li>Bootstrap ClassLoader</li>
</ul>
<p>这是加载器中的大 Boss，任何类的加载行为，都要经它过问。它的作用是加载核心类库，也就是 rt.jar、resources.jar、charsets.jar 等。当然这些 jar 包的路径是可以指定的，-Xbootclasspath 参数可以完成指定操作。</p>
<p>这个加载器是 C++ 编写的，随着 JVM 启动。</p>
<ul>
<li>Extention ClassLoader</li>
</ul>
<p>扩展类加载器，主要用于加载 lib/ext 目录下的 jar 包和 .class 文件。同样的，通过系统变量 java.ext.dirs 可以指定这个目录。</p>
<p>这个加载器是个 Java 类，继承自 URLClassLoader。</p>
<ul>
<li>App ClassLoader</li>
</ul>
<p>这是我们写的 Java 类的默认加载器，有时候也叫作 System ClassLoader。一般用来加载 classpath 下的其他所有 jar 包和 .class 文件，我们写的代码，会首先尝试使用这个类加载器进行加载。</p>
<ul>
<li>Custom ClassLoader</li>
</ul>
<p>自定义加载器，支持一些个性化的扩展功能。</p>
<h3>双亲委派机制</h3>
<p>关于双亲委派机制的问题面试中经常会被问到，你可能已经倒背如流了。</p>
<p>双亲委派机制的意思是除了顶层的启动类加载器以外，其余的类加载器，在加载之前，都会委派给它的父加载器进行加载。这样一层层向上传递，直到祖先们都无法胜任，它才会真正的加载。</p>
<p>打个比方。有一个家族，都是一些听话的孩子。孙子想要买一块棒棒糖，最终都要经过爷爷过问，如果力所能及，爷爷就直接帮孙子买了。</p>
<p>但你有没有想过，“类加载的双亲委派机制，双亲在哪里？明明都是单亲？”</p>
<p>我们还是用一张图来讲解。可以看到，除了启动类加载器，每一个加载器都有一个parent，并没有所谓的双亲。但是由于翻译的问题，这个叫法已经非常普遍了，一定要注意背后的差别。</p>
<p><img src="assets/Cgq2xl4cQNeAG0ECAAA_CbVCY1M014.png" alt="img" /></p>
<p>我们可以翻阅 JDK 代码的 ClassLoader#loadClass 方法，来看一下具体的加载过程。和我们描述的一样，它首先使用 parent 尝试进行类加载，parent 失败后才轮到自己。同时，我们也注意到，这个方法是可以被覆盖的，也就是双亲委派机制并不一定生效。</p>
<p><img src="assets/CgpOIF4cQNeACEs8AACe317zgN8195.jpg" alt="img" /></p>
<p>这个模型的好处在于 Java 类有了一种优先级的层次划分关系。比如 Object 类，这个毫无疑问应该交给最上层的加载器进行加载，即使是你覆盖了它，最终也是由系统默认的加载器进行加载的。</p>
<p>如果没有双亲委派模型，就会出现很多个不同的 Object 类，应用程序会一片混乱。</p>
<h3>一些自定义加载器</h3>
<p>下面我们就来聊一聊可以打破双亲委派机制的一些案例。为了支持一些自定义加载类多功能的需求，Java 设计者其实已经作出了一些妥协。</p>
<h4>案例一：tomcat</h4>
<p>tomcat 通过 war 包进行应用的发布，它其实是违反了双亲委派机制原则的。简单看一下 tomcat 类加载器的层次结构。
<img src="assets/Cgq2xl4cQNeAZ4FuAABzsqSozok762.png" alt="img" /></p>
<p>对于一些需要加载的非基础类，会由一个叫作 WebAppClassLoader 的类加载器优先加载。等它加载不到的时候，再交给上层的 ClassLoader 进行加载。这个加载器用来隔绝不同应用的 .class 文件，比如你的两个应用，可能会依赖同一个第三方的不同版本，它们是相互没有影响的。</p>
<p>如何在同一个 JVM 里，运行着不兼容的两个版本，当然是需要自定义加载器才能完成的事。</p>
<p>那么 tomcat 是怎么打破双亲委派机制的呢？可以看图中的 WebAppClassLoader，它加载自己目录下的 .class 文件，并不会传递给父类的加载器。但是，它却可以使用 SharedClassLoader 所加载的类，实现了共享和分离的功能。</p>
<p>但是你自己写一个 ArrayList，放在应用目录里，tomcat 依然不会加载。它只是自定义的加载器顺序不同，但对于顶层来说，还是一样的。</p>
<h4>案例二：SPI</h4>
<p>Java 中有一个 SPI 机制，全称是 Service Provider Interface，是 Java 提供的一套用来被第三方实现或者扩展的 API，它可以用来启用框架扩展和替换组件。</p>
<p>这个说法可能比较晦涩，但是拿我们常用的数据库驱动加载来说，就比较好理解了。在使用 JDBC 写程序之前，通常会调用下面这行代码，用于加载所需要的驱动类。</p>
<pre><code>Class.forName(&quot;com.mysql.jdbc.Driver&quot;)
</code></pre>
<p>这只是一种初始化模式，通过 static 代码块显式地声明了驱动对象，然后把这些信息，保存到底层的一个 List 中。这种方式我们不做过多的介绍，因为这明显就是一个接口编程的思路，没什么好奇怪的。</p>
<p><strong>但是你会发现，即使删除了 Class.forName 这一行代码，也能加载到正确的驱动类，什么都不需要做，非常的神奇，它是怎么做到的呢？</strong></p>
<p>我们翻开 MySQL 的驱动代码，发现了一个奇怪的文件。之所以能够发生这样神奇的事情，就是在这里实现的。</p>
<p>路径：</p>
<pre><code>mysql-connector-java-8.0.15.jar!/META-INF/services/java.sql.Driver
</code></pre>
<p>里面的内容是：</p>
<pre><code>com.mysql.cj.jdbc.Driver
</code></pre>
<p>通过在 META-INF/services 目录下，创建一个以接口全限定名为命名的文件（内容为实现类的全限定名），即可自动加载这一种实现，这就是 SPI。</p>
<p>SPI 实际上是“基于接口的编程＋策略模式＋配置文件”组合实现的动态加载机制，主要使用 java.util.ServiceLoader 类进行动态装载。</p>
<p><img src="assets/CgpOIF4cQNeARP3IAAA2VH9MXoY723.jpg" alt="img" /></p>
<p>这种方式，同样打破了双亲委派的机制。</p>
<p>DriverManager 类和 ServiceLoader 类都是属于 rt.jar 的。它们的类加载器是 Bootstrap ClassLoader，也就是最上层的那个。而具体的数据库驱动，却属于业务代码，这个启动类加载器是无法加载的。这就比较尴尬了，虽然凡事都要祖先过问，但祖先没有能力去做这件事情，怎么办？</p>
<p>我们可以一步步跟踪代码，来看一下这个过程。</p>
<pre><code>//part1:DriverManager::loadInitialDrivers

  //jdk1.8 之后，变成了lazy的ensureDriversInitialized

  ...

  ServiceLoader &lt;Driver&gt; loadedDrivers = ServiceLoader.load(Driver.class);

  Iterator&lt;Driver&gt; driversIterator = loadedDrivers.iterator();

  ...

  //part2:ServiceLoader::load

  public static &lt;T&gt; ServiceLoader&lt;T&gt; load(Class&lt;T&gt; service) {

      ClassLoader cl = Thread.currentThread().getContextClassLoader();

      return ServiceLoader.load(service, cl);

  }
</code></pre>
<p>通过代码你可以发现 Java 玩了个魔术，它把当前的类加载器，设置成了线程的上下文类加载器。那么，对于一个刚刚启动的应用程序来说，它当前的加载器是谁呢？也就是说，启动 main 方法的那个加载器，到底是哪一个？</p>
<p>所以我们继续跟踪代码。找到 Launcher 类，就是 jre 中用于启动入口函数 main 的类。我们在 Launcher 中找到以下代码。</p>
<pre><code>public Launcher() {

 Launcher.ExtClassLoader var1;

 try {

     var1 = Launcher.ExtClassLoader.getExtClassLoader();

 } catch (IOException var10) {

     throw new InternalError(&quot;Could not create extension class loader&quot;, var10);

 }
 try {

     this.loader = Launcher.AppClassLoader.getAppClassLoader(var1);

 } catch (IOException var9) {

     throw new InternalError(&quot;Could not create application class loader&quot;, var9);

 }

 Thread.currentThread().setContextClassLoader(this.loader);

 ...

 }
</code></pre>
<p>到此为止，事情就比较明朗了，当前线程上下文的类加载器，是应用程序类加载器。使用它来加载第三方驱动，是没有什么问题的。</p>
<p>我们之所以花大量的篇幅来介绍这个过程，第一，可以让你更好的看到一个打破规则的案例。第二，这个问题面试时出现的几率也是比较高的，你需要好好理解。</p>
<h4>案例三：OSGi</h4>
<p>OSGi 曾经非常流行，Eclipse 就使用 OSGi 作为插件系统的基础。OSGi 是服务平台的规范，旨在用于需要长运行时间、动态更新和对运行环境破坏最小的系统。</p>
<p>OSGi 规范定义了很多关于包生命周期，以及基础架构和绑定包的交互方式。这些规则，通过使用特殊 Java 类加载器来强制执行，比较霸道。</p>
<p>比如，在一般 Java 应用程序中，classpath 中的所有类都对所有其他类可见，这是毋庸置疑的。但是，OSGi 类加载器基于 OSGi 规范和每个绑定包的 manifest.mf 文件中指定的选项，来限制这些类的交互，这就让编程风格变得非常的怪异。但我们不难想象，这种与直觉相违背的加载方式，肯定是由专用的类加载器来实现的。</p>
<p>随着 jigsaw 的发展（旨在为 Java SE 平台设计、实现一个标准的模块系统），我个人认为，现在的 OSGi，意义已经不是很大了。OSGi 是一个庞大的话题，你只需要知道，有这么一个复杂的东西，实现了模块化，每个模块可以独立安装、启动、停止、卸载，就可以了。</p>
<p>不过，如果你有机会接触相关方面的工作，也许会不由的发出感叹：原来 Java 的类加载器，可以玩出这么多花样。</p>
<h3>如何替换 JDK 的类</h3>
<p>让我们回到本课时开始的问题，如何替换 JDK 中的类？比如，我们现在就拿 HashMap为例。</p>
<p>当 Java 的原生 API 不能满足需求时，比如我们要修改 HashMap 类，就必须要使用到 Java 的 endorsed 技术。我们需要将自己的 HashMap 类，打包成一个 jar 包，然后放到 -Djava.endorsed.dirs 指定的目录中。注意类名和包名，应该和 JDK 自带的是一样的。但是，java.lang 包下面的类除外，因为这些都是特殊保护的。</p>
<p>因为我们上面提到的双亲委派机制，是无法直接在应用中替换 JDK 的原生类的。但是，有时候又不得不进行一下增强、替换，比如你想要调试一段代码，或者比 Java 团队早发现了一个 Bug。所以，Java 提供了 endorsed 技术，用于替换这些类。这个目录下的 jar 包，会比 rt.jar 中的文件，优先级更高，可以被最先加载到。</p>
<h3>小结</h3>
<p>通过本课时的学习我们可以了解到，一个 Java 类的加载，经过了加载、验证、准备、解析、初始化几个过程，每一个过程都划清了各自负责的事情。</p>
<p>接下来，我们了解到 Java 自带的三个类加载器。同时了解到，main 方法的线程上下文加载器，其实是 Application ClassLoader。</p>
<p>一般情况下，类加载是遵循双亲委派机制的。我们也认识到，这个双亲，很有问题。通过 3 个案例的学习和介绍，可以看到有很多打破这个规则的情况。类加载器通过开放的 API，让加载过程更加灵活。</p>
<p>Java 的类加载器是非常重要的知识点，也是面试常考的知识点，本课时提供了多个面试题，你可以实际操作体验一下。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="02&#32;大厂面试题：你不得不掌握的&#32;JVM&#32;内存管理.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="04&#32;动手实践：从栈帧看字节码是如何在&#32;JVM&#32;中进行流转的.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43587fdac3645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
</body>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-NPSEEVD756"></script>
<script>
    window.dataLayer = window.dataLayer || [];

    function gtag() {
        dataLayer.push(arguments);
    }

    gtag('js', new Date());
    gtag('config', 'G-NPSEEVD756');
    var path = window.location.pathname
    var cookie = getCookie("lastPath");
    console.log(path)
    if (path.replace("/", "") === "") {
        if (cookie.replace("/", "") !== "") {
            console.log(cookie)
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E6%B7%B1%E5%85%A5%E6%B5%85%E5%87%BA%20Java%20%E8%99%9A%E6%8B%9F%E6%9C%BA-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
        }
    } else {
        setCookie("lastPath", path)
    }

    function setCookie(cname, cvalue) {
        var d = new Date();
        d.setTime(d.getTime() + (180 * 24 * 60 * 60 * 1000));
        var expires = "expires=" + d.toGMTString();
        document.cookie = cname + "=" + cvalue + "; " + expires + ";path = /";
    }

    function getCookie(cname) {
        var name = cname + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i].trim();
            if (c.indexOf(name) === 0) return c.substring(name.length, c.length);
        }
        return "";
    }
</script>

</html>
