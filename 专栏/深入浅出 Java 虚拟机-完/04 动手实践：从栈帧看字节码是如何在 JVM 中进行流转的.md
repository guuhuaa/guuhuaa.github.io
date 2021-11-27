<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>04 动手实践：从栈帧看字节码是如何在 JVM 中进行流转的.md</title>
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

                    
                    <a href="03&#32;大厂面试题：从覆盖&#32;JDK&#32;的类开始掌握类的加载机制.md">03 大厂面试题：从覆盖 JDK 的类开始掌握类的加载机制.md</a>

                </li>
                <li>

                    <a class="current-tab" href="04&#32;动手实践：从栈帧看字节码是如何在&#32;JVM&#32;中进行流转的.md">04 动手实践：从栈帧看字节码是如何在 JVM 中进行流转的.md</a>
                    

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
                        <div><h1>04 动手实践：从栈帧看字节码是如何在 JVM 中进行流转的</h1>
<p>在上一课时我们掌握了 JVM 的内存区域划分，以及 .class 文件的加载机制。也了解到很多初始化动作是在不同的阶段发生的。</p>
<p>但你可能仍对以下这些问题有疑问：</p>
<ul>
<li>怎么查看字节码文件？</li>
<li>字节码文件长什么样子？</li>
<li>对象初始化之后，具体的字节码又是怎么执行的？</li>
</ul>
<p>带着这些疑问，我们进入本课时的学习，本课时将带你动手实践，详细分析一个 Java 文件产生的字节码，并从栈帧层面看一下字节码的具体执行过程。</p>
<h3>工具介绍</h3>
<p>工欲善其事，必先利其器。在开始本课时的内容之前，先给你介绍两个分析字节码的小工具。</p>
<h4>javap</h4>
<p>第一个小工具是 javap，javap 是 JDK 自带的反解析工具。它的作用是将 .class 字节码文件解析成可读的文件格式。我们在第一课时，就是用的它输出了 HelloWorld 的内容。</p>
<p>在使用 javap 时我一般会添加 -v 参数，尽量多打印一些信息。同时，我也会使用 -p 参数，打印一些私有的字段和方法。使用起来大概是这样：</p>
<pre><code class="language-java">javap -p -v HelloWorld
</code></pre>
<p>在 Stack Overflow 上有一个非常有意思的问题：我在某个类中增加一行注释之后，为什么两次生成的 .class 文件，它们的 MD5 是不一样的？</p>
<p>这是因为在 javac 中可以指定一些额外的内容输出到字节码。经常用的有</p>
<ul>
<li><strong>javac -g:lines</strong> 强制生成 LineNumberTable。</li>
<li><strong>javac -g:vars</strong>  强制生成 LocalVariableTable。</li>
<li><strong>javac -g</strong> 生成所有的 debug 信息。</li>
</ul>
<p>为了观察字节码的流转，我们本课时就会使用到这些参数。</p>
<h4>jclasslib</h4>
<p>如果你不太习惯使用命令行的操作，还可以使用 jclasslib，jclasslib 是一个图形化的工具，能够更加直观的查看字节码中的内容。它还分门别类的对类中的各个部分进行了整理，非常的人性化。同时，它还提供了 Idea 的插件，你可以从 plugins 中搜索到它。</p>
<p>如果你在其中看不到一些诸如 LocalVariableTable 的信息，记得在编译代码的时候加上我们上面提到的这些参数。</p>
<p>jclasslib 的下载地址：<a href="https://github.com/ingokegel/jclasslib">https://github.com/ingokegel/jclasslib</a></p>
<h3>类加载和对象创建的时机</h3>
<p>接下来，我们来看一个稍微复杂的例子，来具体看一下类加载和对象创建的过程。</p>
<p>首先，我们写一个最简单的 Java 程序 A.java。它有一个公共方法 test，还有一个静态成员变量和动态成员变量。</p>
<pre><code class="language-java">class B {

    private int a = 1234;

    static long C = 1111;

    public long test(long num) {

        long ret = this.a + num + C;

        return ret;

    }

}

public class A {

    private B b = new B();

    public static void main(String[] args) {

        A a = new A();

        long num = 4321 ;

        long ret = a.b.test(num);

        System.out.println(ret);

    }

}
</code></pre>
<p>前面我们提到，类的初始化发生在类加载阶段，那对象都有哪些创建方式呢？除了我们常用的 new，还有下面这些方式：</p>
<ul>
<li>使用 Class 的 newInstance 方法。</li>
<li>使用 Constructor 类的 newInstance 方法。</li>
<li>反序列化。</li>
<li>使用 Object 的 clone 方法。</li>
</ul>
<p>其中，后面两种方式没有调用到构造函数。</p>
<p>当虚拟机遇到一条 new 指令时，首先会检查这个指令的参数能否在常量池中定位一个符号引用。然后检查这个符号引用的类字节码是否加载、解析和初始化。如果没有，将执行对应的类加载过程。</p>
<p>拿我们上面的代码来说，执行 A 代码，在调用 private B b = new B() 时，就会触发 B 类的加载。</p>
<p><img src="assets/CgpOIF4ezuOAK_6bAACFY5oeX-Y174.jpg" alt="img" /></p>
<p>让我们结合上图回顾一下前面章节的内容。A 和 B 会被加载到元空间的方法区，进入 main 方法后，将会交给执行引擎执行。这个执行过程是在栈上完成的，其中有几个重要的区域，包括虚拟机栈、程序计数器等。接下来我们详细看一下虚拟机栈上的执行过程。</p>
<h3>查看字节码</h3>
<h4>命令行查看字节码</h4>
<p>使用下面的命令编译源代码 A.java。如果你用的是 Idea，可以直接将参数追加在 VM options 里面。</p>
<pre><code class="language-java">javac -g:lines -g:vars A.java
</code></pre>
<p>这将强制生成 LineNumberTable 和 LocalVariableTable。</p>
<p>然后使用 javap 命令查看 A 和 B 的字节码。</p>
<pre><code class="language-java">javap -p -v A

javap -p -v B
</code></pre>
<p>这个命令，不仅会输出行号、本地变量表信息、反编译汇编代码，还会输出当前类用到的常量池等信息。由于内容很长，这里就不具体展示了，你可以使用上面的命令实际操作一下就可以了。</p>
<p>注意 javap 中的如下字样。</p>
<p><strong>&lt;1&gt;</strong></p>
<pre><code class="language-js">1: invokespecial #1   // Method java/lang/Object.&quot;&lt;init&gt;&quot;:()V
</code></pre>
<p>可以看到对象的初始化，首先是调用了 Object 类的初始化方法。注意这里是 <init> 而不是 <cinit>。</p>
<p><strong>&lt;2&gt;</strong></p>
<pre><code class="language-java">#2 = Fieldref           #6.#27         // B.a:I
</code></pre>
<p>它其实直接拼接了 #13 和 #14 的内容。</p>
<pre><code class="language-java">#6 = Class             #29           // B

#27 = NameAndType       #8:#9         // a:I

...

#8 = Utf8               a

#9 = Utf8               I
</code></pre>
<p><strong>&lt;3&gt;</strong></p>
<p>你会注意到 :I 这样特殊的字符。它们也是有意义的，如果你经常使用 jmap 这种命令，应该不会陌生。大体包括：</p>
<ul>
<li>B 基本类型 byte</li>
<li>C 基本类型 char</li>
<li>D 基本类型 double</li>
<li>F 基本类型 float</li>
<li>I 基本类型 int</li>
<li>J 基本类型 long</li>
<li>S 基本类型 short</li>
<li>Z 基本类型 boolean</li>
<li>V 特殊类型 void</li>
<li>L 对象类型，以分号结尾，如 Ljava/lang/Object;</li>
<li>[Ljava/lang/String; 数组类型，每一位使用一个前置的&quot;[&quot;字符来描述</li>
</ul>
<p>我们注意到 code 区域，有非常多的二进制指令。如果你接触过汇编语言，会发现它们之间其实有一定的相似性。但这些二进制指令，并不是操作系统能够认识的，它们是提供给 JVM 运行的源材料。</p>
<h4>可视化查看字节码</h4>
<p>接下来，我们就可以使用更加直观的工具 jclasslib，来查看字节码中的具体内容了。</p>
<p>我们以 B.class 文件为例，来查看它的内容。</p>
<p><strong>&lt;1&gt;</strong></p>
<p>首先，我们能够看到 Constant Pool（常量池），这些内容，就存放于我们的 Metaspace 区域，属于非堆。</p>
<p><img src="assets/Cgq2xl4ezeKAWB30AADZXqT3TjQ870.jpg" alt="img" /></p>
<p>常量池包含 .class 文件常量池、运行时常量池、String 常量池等部分，大多是一些静态内容。</p>
<p><strong>&lt;2&gt;</strong></p>
<p>接下来，可以看到两个默认的 <init> 和 <cinit> 方法。以下截图是 test 方法的 code 区域，比命令行版的更加直观。</p>
<p><img src="assets/CgpOIF4ezeKAVmSnAACExsXdgtg544.jpg" alt="img" /></p>
<p><strong>&lt;3&gt;</strong></p>
<p>继续往下看，我们看到了 LocalVariableTable 的三个变量。其中，slot 0 指向的是 this 关键字。该属性的作用是描述帧栈中局部变量与源码中定义的变量之间的关系。如果没有这些信息，那么在 IDE 中引用这个方法时，将无法获取到方法名，取而代之的则是 arg0 这样的变量名。</p>
<p><img src="assets/Cgq2xl4ezeKASWJHAAB5Ptt1JsM137.jpg" alt="img" /></p>
<p>本地变量表的 slot 是可以复用的。注意一个有意思的地方，index 的最大值为 3，证明了本地变量表同时最多能够存放 4 个变量。</p>
<p>另外，我们观察到还有 LineNumberTable 等选项。该属性的作用是描述源码行号与字节码行号（字节码偏移量）之间的对应关系，有了这些信息，在 debug 时，就能够获取到发生异常的源代码行号。</p>
<h3>test 函数执行过程</h3>
<h4>Code 区域介绍</h4>
<p>test 函数同时使用了成员变量 a、静态变量 C，以及输入参数 num。我们此时说的函数执行，内存其实就是在虚拟机栈上分配的。下面这些内容，就是 test 方法的字节码。</p>
<pre><code class="language-c">public long test(long);

   descriptor: (J)J

   flags: ACC_PUBLIC

   Code:

     stack=4, locals=5, args_size=2

        0: aload_0

        1: getfield      #2                  // Field a:I

        4: i2l

        5: lload_1

        6: ladd

        7: getstatic     #3                  // Field C:J

       10: ladd

       11: lstore_3

       12: lload_3

       13: lreturn

     LineNumberTable:

       line 13: 0

       line 14: 12

     LocalVariableTable:

       Start  Length  Slot  Name   Signature

           0      14     0  this   LB;

           0      14     1   num   J

          12       2     3   ret   J
</code></pre>
<p>我们介绍一下比较重要的 3 三个数值。
<strong>&lt;1&gt;</strong></p>
<p>首先，注意 stack 字样，它此时的数值为 4，表明了 test 方法的最大操作数栈深度为 4。JVM 运行时，会根据这个数值，来分配栈帧中操作栈的深度。</p>
<p><strong>&lt;2&gt;</strong></p>
<p>相对应的，locals 变量存储了局部变量的存储空间。它的单位是 Slot（槽），可以被重用。其中存放的内容，包括：</p>
<ul>
<li>this</li>
<li>方法参数</li>
<li>异常处理器的参数</li>
<li>方法体中定义的局部变量</li>
</ul>
<p><strong>&lt;3&gt;</strong></p>
<p>args_size 就比较好理解。它指的是方法的参数个数，因为每个方法都有一个隐藏参数 this，所以这里的数字是 2。</p>
<h4>字节码执行过程</h4>
<p>我们稍微回顾一下 JVM 运行时的相关内容。main 线程会拥有两个主要的运行时区域：Java 虚拟机栈和程序计数器。其中，虚拟机栈中的每一项内容叫作栈帧，栈帧中包含四项内容：局部变量报表、操作数栈、动态链接和完成出口。</p>
<p>我们的字节码指令，就是靠操作这些数据结构运行的。下面我们看一下具体的字节码指令。</p>
<p><img src="assets/CgpOIF4ezeKAHVCXAABv7rzSgXE896.jpg" alt="img" /></p>
<p>（1）<strong>0: aload_0</strong></p>
<p>把第 1 个引用型局部变量推到操作数栈，这里的意思是把 this 装载到了操作数栈中。</p>
<p>对于 static 方法，aload_0 表示对方法的第一个参数的操作。</p>
<p><img src="assets/CgpOIF4w-GGAA6DnAAEtqWkdOnE696.jpg" alt="img" /></p>
<p>（2）<strong>1: getfield      #2</strong></p>
<p>将栈顶的指定的对象的第 2 个实例域（Field）的值，压入栈顶。#2 就是指的我们的成员变量 a。</p>
<pre><code class="language-c">#2 = Fieldref           #6.#27         // B.a:I

...

#6 = Class             #29           // B

#27 = NameAndType       #8:#9         // a:I
</code></pre>
<p><img src="assets/Cgq2xl4w-HKABrhgAAEvNAmbGWY870.jpg" alt="img" /></p>
<p>（3）<strong>i2l</strong></p>
<p>将栈顶 int 类型的数据转化为 long 类型，这里就涉及我们的隐式类型转换了。图中的信息没有变动，不再详解介绍。</p>
<p>（4）<strong>lload_1</strong></p>
<p>将第一个局部变量入栈。也就是我们的参数 num。这里的 l 表示 long，同样用于局部变量装载。你会看到这个位置的局部变量，一开始就已经有值了。</p>
<p><img src="assets/CgpOIF4w-IuAOmp0AAEzFWM0gmc155.jpg" alt="img" /></p>
<p>（5）<strong>ladd</strong></p>
<p>把栈顶两个 long 型数值出栈后相加，并将结果入栈。</p>
<p><img src="assets/Cgq2xl4w-KKAGhwcAAEtNkzwpcw021.jpg" alt="img" /></p>
<p>（6）<strong>getstatic #3</strong></p>
<p>根据偏移获取静态属性的值，并把这个值 push 到操作数栈上。</p>
<p><img src="assets/Cgq2xl4w-MWAVt_ZAAE2NxokOfU153.jpg" alt="img" /></p>
<p>（7）<strong>ladd</strong></p>
<p>再次执行 ladd。</p>
<p><img src="assets/CgpOIF4w-NCAaU4rAAEtel-Iskk153.jpg" alt="img" /></p>
<p>（8）<strong>lstore_3</strong></p>
<p>把栈顶 long 型数值存入第 4 个局部变量。</p>
<p>还记得我们上面的图么？slot 为 4，索引为 3 的就是 ret 变量。</p>
<p><img src="assets/CgpOIF4w-OWAPOn9AAE1Y2sXttM659.jpg" alt="img" /></p>
<p>（9）<strong>lload_3</strong></p>
<p>正好与上面相反。上面是变量存入，我们现在要做的，就是把这个变量 ret，压入虚拟机栈中。</p>
<p><img src="assets/CgpOIF4w-O6ARdRFAAE62GkvYGo689.jpg" alt="img" /></p>
<p>（10）<strong>lreturn</strong></p>
<p>从当前方法返回 long。</p>
<p>到此为止，我们的函数就完成了相加动作，执行成功了。JVM 为我们提供了非常丰富的字节码指令。详细的字节码指令列表，可以参考以下网址：</p>
<p><a href="https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-6.html">https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-6.html</a></p>
<h4>注意点</h4>
<p>注意上面的第 8 步，我们首先把变量存放到了变量报表，然后又拿出这个值，把它入栈。为什么会有这种多此一举的操作？原因就在于我们定义了 ret 变量。JVM 不知道后面还会不会用到这个变量，所以只好傻瓜式的顺序执行。</p>
<p>为了看到这些差异。大家可以把我们的程序稍微改动一下，直接返回这个值。</p>
<pre><code class="language-java">public long test(long num) {

       return this.a + num + C;

}
</code></pre>
<p>再次看下，对应的字节码指令是不是简单了很多？</p>
<pre><code class="language-c">0: aload_0

1: getfield     #2                 // Field a:I

4: i2l

5: lload_1

6: ladd

7: getstatic     #3                 // Field C:J

10: ladd

11: lreturn
</code></pre>
<p>那我们以后编写程序时，是不是要尽量少的定义成员变量？</p>
<p>这是没有必要的。栈的操作复杂度是 O(1)，对我们的程序性能几乎没有影响。平常的代码编写，还是以可读性作为首要任务。</p>
<h3>小结</h3>
<p>本课时，我们学会了使用 javap 和 jclasslib 两个工具。平常工作中，掌握第一个就够了，后者主要为我们提供更加直观的展示。</p>
<p>我们从实际分析一段代码开始，详细介绍了几个字节码指令对程序计数器、局部变量表、操作数栈等内容的影响，初步接触了 Java 的字节码文件格式。</p>
<p>希望你能够建立起一个运行时的脉络，在看到相关的 opcode 时，能够举一反三的思考背后对这些数据结构的操作。这样理解的字节码指令，根本不会忘。</p>
<p>你还可以尝试着对 A 类的代码进行分析，我们这里先留下一个悬念。课程后面会详细介绍 JVM 在方法调用上的一些特点。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="03&#32;大厂面试题：从覆盖&#32;JDK&#32;的类开始掌握类的加载机制.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="05&#32;大厂面试题：得心应手应对&#32;OOM&#32;的疑难杂症.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435889a810645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
