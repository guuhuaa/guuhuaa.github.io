<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>23 动手实践：JIT 参数配置如何影响程序运行？.md</title>
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

                    <a class="current-tab" href="23&#32;动手实践：JIT&#32;参数配置如何影响程序运行？.md">23 动手实践：JIT 参数配置如何影响程序运行？.md</a>
                    

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
                        <div><h1>23 动手实践：JIT 参数配置如何影响程序运行？</h1>
<p>本课时我们主要分享一个实践案例，JIT 参数配置是如何影响程序运行的。</p>
<p>我们在前面的课时中介绍了很多字节码指令，这也是 Java 能够跨平台的保证。程序在运行的时候，这些指令会按照顺序解释执行，但是，这种解释执行的方式是非常低效的，它需要把字节码先<strong>翻译</strong>成机器码，才能往下执行。另外，字节码是 Java 编译器做的一次初级优化，许多代码可以满足语法分析，但还有很大的优化空间。</p>
<p>所以，为了提高热点代码的执行效率，在运行时，虚拟机将会把这些代码编译成与本地平台相关的机器码，并进行各种层次的优化。完成这个任务的编译器，就称为<strong>即时编译器</strong>（Just In Time Compiler），简称 <strong>JIT 编译器</strong>。</p>
<p>热点代码，就是那些被频繁调用的代码，比如调用次数很高或者在 for 循环里的那些代码。这些再次编译后的机器码会被缓存起来，以备下次使用，但对于那些执行次数很少的代码来说，这种编译动作就纯属浪费。</p>
<p>在第 14 课时我们提到了参数“-XX:ReservedCodeCacheSize”，用来限制 CodeCache 的大小。也就是说，JIT 编译后的代码都会放在 CodeCache 里。</p>
<p>如果这个空间不足，JIT 就无法继续编译，编译执行会变成解释执行，性能会降低一个数量级。同时，JIT 编译器会一直尝试去优化代码，从而造成了 CPU 占用上升。</p>
<p><img src="assets/Cgq2xl57A7qAGBF6AAAx8j1m3Kw525.jpg" alt="img" /></p>
<h2>JITWatch</h2>
<p>在开始之前，我们首先介绍一个观察 JIT 执行过程的图形化工具：JITWatch，这个工具非常好用，可以解析 JIT 的日志并友好地展示出来。<a href="https://github.com/AdoptOpenJDK/jitwatch">项目地址请点击这里查看</a>。</p>
<p>下载之后，进入解压目录，执行 ant 即可编译出执行文件。</p>
<h3>产生 JIT 日志</h3>
<p>我们观察下面的一段代码，这段代码没有什么意义，而且写得很烂。在 test 函数中循环 cal 函数 1 千万次，在 cal 函数中，还有一些冗余的上锁操作和赋值操作，这些操作在解释执行的时候，会加重 JVM 的负担。</p>
<pre><code>public class JITDemo {
    Integer a = 1000;

    public void setA(Integer a) {
        this.a = a;    }

    public Integer getA() {
        return this.a;
    }

    public Integer cal(int num) {
        synchronized (new Object()) {
            Integer a = getA();
            int b = a * 10;
            b = a * 100;
            return b + num;
        }
    }

    public int test() {
        synchronized (new Object()) {
            int total = 0;
            int count = 100_000_00;
            for (int i = 0; i &lt; count; i++) {
                total += cal(i);
                if (i % 1000 == 0) {
                    System.out.println(i * 1000);
                }
            }
            return total;
        }
    }

    public static void main(String[] args) {
        JITDemo demo = new JITDemo();
        int total = demo.test();
</code></pre>
<p>在方法执行的时候，我们加上一系列参数，用来打印 JIT 最终生成的机器码，执行命令如下所示：</p>
<pre><code>$JAVA_HOME_13/bin/java -server -XX:+UnlockDiagnosticVMOptions -XX:+TraceClassLoading  -XX:+PrintAssembly -XX:+LogCompilation -XX:LogFile=jitdemo.log JITDemo
</code></pre>
<p>执行的过程，会输入到 jitdemo.log 文件里，接下来我们分析这个文件。</p>
<h3>使用</h3>
<p><img src="assets/Ciqah157A7uAPt49AAD7831CinU309.jpg" alt="img" /></p>
<p>单击 open log 按钮，打开我们生成的日志文件。</p>
<p><img src="assets/Cgq2xl57A7uAf1o-AAEJfdrafg8749.jpg" alt="img" /></p>
<p>单击 config 按钮，加入要分析的源代码目录和字节码目录。确认后，单击 start 按钮进行分析。</p>
<p>在右侧找到我们的 test 方法，聚焦光标后，将弹出我们要分析的主要界面。</p>
<p><img src="assets/Ciqah157A7uAB8iPAAFu7HBxG4w040.jpg" alt="img" /></p>
<p>在同一个界面上，我们能够看到源代码、字节码、机器码的对应关系。在右上角，还有 C2/OSR/Level4 这样的字样，可以单击切换。</p>
<p>单击上图中的 Chain 按钮，还会弹出一个依赖链界面，该界面显示了哪些方法已经被编译了、哪些被内联、哪些是通过普通的方法调用运行的。</p>
<p><img src="assets/Cgq2xl57A7uAO1CdAACX4fWefMo181.jpg" alt="img" /></p>
<p>使用 JITWatch 可以看到，调用了 1 千万次的 for 循环代码，已经被 C2 进行编译了。</p>
<p><img src="assets/Cgq2xl57A7yAZvChAAG-RAna12A372.jpg" alt="img" /></p>
<h2>编译层次</h2>
<p>HotSpot 虚拟机包含多个即时编译器，有 C1、C2 和 Graal，采用的是分层编译的模式。使用 jstack 获得的线程信息，经常能看到它们的身影。</p>
<p>实验性质的 Graal 可以通过追加 JVM 参数进行开启，命令行如下：</p>
<pre><code>$JAVA_HOME_13/bin/java -server -XX:+UnlockDiagnosticVMOptions -XX:+TraceClassLoading
  -XX:+PrintAssembly -XX:+LogCompilation -XX:+UnlockExperimentalVMOptions
   -XX:+UseJVMCICompiler -XX:LogFile=jitdemo.log JITDemo
</code></pre>
<p>不同层次的编译器会产生不一样的效果，机器码也会不同，我们仅看 C1、C2 的一些特点。</p>
<p>JIT 编译方式有两种：一种是编译方法，另一种是编译循环。分层编译将 JVM 的执行状态分为了五个层次：</p>
<ul>
<li>字节码的解释执行；</li>
<li>执行不带 profiling 的 C1 代码；</li>
<li>执行仅带方法调用次数，以及循环执行次数 profiling 的 C1 代码；</li>
<li>执行带所有 profiling 的 C1 代码；</li>
<li>执行 C2 代码。</li>
</ul>
<p>其中，profiling 指的是运行时的程序执行状态数据，比如循环调用的次数、方法调用的次数、分支跳转次数、类型转换次数等。JDK 中的 hprof 工具就是一种 profiler。</p>
<p>在不启用分层编译的情况下，当方法的调用次数和循环回边的次数总和，超过由参数 -XX:CompileThreshold 指定的阈值时，便会触发即时编译；当启用分层编译时，这个参数将会失效，会采用动态调整的方式进行。</p>
<p>常见的优化方法有以下几种：</p>
<ul>
<li>公共子表达式消除</li>
<li>数组范围检查消除</li>
<li>方法内联</li>
<li>逃逸分析</li>
</ul>
<p>我们重点看一下方法内联和逃逸分析。</p>
<h2>方法内联</h2>
<p>在第 17 课时里，我们可以看到方法调用的开销是比较大的，尤其是在调用量非常大的情况下。拿简单的 getter/setter 方法来说，这种方法在 Java 代码中大量存在，我们在访问的时候，需要创建相应的栈帧，访问到需要的字段后，再弹出栈帧，恢复原程序的执行。</p>
<p>如果能够把这些对象的访问和操作，纳入到目标方法的调用范围之内，就少了一次方法调用，速度就能得到提升，这就是方法内联的概念。</p>
<p>C2 编译器会在解析字节码的过程中完成方法内联。内联后的代码和调用方法的代码，会组成新的机器码，存放在 CodeCache 区域里。</p>
<p>在 JDK 的源码里，有很多被 <strong>@ForceInline</strong> 注解的方法，这些方法会在执行的时候被强制进行内联；而被 <strong>@DontInline</strong> 注解的方法，则始终不会被内联，比如下面的一段代码。</p>
<p>java.lang.ClassLoader 的 getClassLoader 方法将会被强制内联。</p>
<pre><code>@CallerSensitive
    @ForceInline // to ensure Reflection.getCallerClass optimization
    public ClassLoader getClassLoader() {
        ClassLoader cl = getClassLoader0();
        if (cl == null)
            return null;
        SecurityManager sm = System.getSecurityManager();
        if (sm != null) {
            ClassLoader.checkClassLoaderPermission(cl, Reflection.getCallerClass());
        }
        return cl;
}
</code></pre>
<p>方法内联的过程是非常智能的，内联后的代码，会按照一定规则进行再次优化。最终的机器码，在保证逻辑正确的前提下，可能和我们推理的完全不一样。在非常小的概率下，JIT 会出现 Bug，这时候可以关闭问题方法的内联，或者直接关闭 JIT 的优化，保持解释执行。实际上，这种 Bug 我从来没碰到过。</p>
<pre><code>-XX:CompileCommand=exclude,com/lagou/Test,test
</code></pre>
<p>上面的参数，表示 com.lagou.Test 的 test 方法将不会进行 JIT 编译，一直解释执行。</p>
<p>另外，C2 支持的内联层次不超过 9 层，太高的话，CodeCache 区域会被挤爆，这个阈值可以通过 -XX:MaxInlineLevel 进行调整。相似的，编译后的代码超过一定大小也不会再内联，这个参数由 -XX:InlineSmallCode 进行调整。</p>
<p>有非常多的参数，被用来控制对内联方法的选择，整体来说，短小精悍的小方法更容易被优化。</p>
<p>这和我们在日常中的编码要求是一致的：代码块精简，逻辑清晰的代码，更容易获得优化的空间。</p>
<p><img src="assets/Ciqah157A7yAJiHeAAF5gyjxA3w172.jpg" alt="img" /></p>
<p>我们使用 JITWatch 再看一下对于 getA() 方法的调用，将鼠标悬浮在字节码指令上，可以看到方法已经被内联了。</p>
<h2>逃逸分析</h2>
<p>逃逸分析（Escape Analysis）是目前 JVM 中比较前沿的优化技术。通过逃逸分析，JVM 能够分析出一个新的对象使用范围，从而决定是否要将这个对象分配到堆上。</p>
<p>使用 -XX:+DoEscapeAnalysis 参数可以开启逃逸分析，逃逸分析现在是 JVM 的默认行为，这个参数可以忽略。</p>
<p>JVM 判断新创建的对象是否逃逸的依据有：</p>
<ul>
<li>对象被赋值给堆中对象的字段和类的静态变量；</li>
<li>对象被传进了不确定的代码中去运行。</li>
</ul>
<p>举个例子，在代码 1 中，虽然 map 是一个局部变量，但是它通过 return 语句返回，其他外部方法可能会使用它，这就是方法逃逸。另外，如果被其他线程引用或者赋值，则成为线程逃逸。</p>
<p>代码 2，用完 Map 之后就直接销毁了，我们就可以说 map 对象没有逃逸。</p>
<p>代码1：</p>
<pre><code>public Map fig(){
    Map map = new HashMap();
    ...
    return map;
}
</code></pre>
<p>代码2：</p>
<pre><code>public void fig(){
    Map map = new HashMap();
    ...
}
</code></pre>
<p>那逃逸分析有什么好处呢？</p>
<ul>
<li><strong>同步省略</strong>，如果一个对象被发现只能从一个线程被访问到，那么对于这个对象的操作可以不考虑同步。</li>
<li><strong>栈上分配</strong>，如果一个对象在子程序中被分配，那么指向该对象的指针永远不会逃逸，对象有可能会被优化为栈分配。</li>
<li><strong>分离对象或标量替换</strong>，有的对象可能不需要作为一个连续的内存结构存在也可以被访问到，那么对象的部分（或全部）可以不存储在内存，而是存储在 CPU 寄存器中。标量是指无法再分解的数据类型，比如原始数据类型及 reference 类型。</li>
</ul>
<p><img src="assets/Cgq2xl57A7yAZKc2AAFu39pb5SE629.jpg" alt="img" /></p>
<p>再来看一下 JITWatch 对 synchronized 代码块的分析。根据提示，由于逃逸分析了解到新建的锁对象 Object 并没有逃逸出方法 cal，它将会在栈上直接分配。</p>
<p>查看 C2 编译后的机器码，发现并没有同步代码相关的生成。这是因为 JIT 在分析之后，发现针对 new Object() 这个对象并没有发生线程竞争的情况，则会把这部分的同步直接给优化掉。我们在代码层次做了一些无用功，字节码无法发现它，而 JIT 智能地找到了它并进行了优化。</p>
<p>因此，并不是所有的对象或者数组都会在堆上分配。由于 JIT 的存在，如果发现某些对象没有逃逸出方法，那么就有可能被优化成栈分配。</p>
<h2>intrinsic</h2>
<p>另外一个不得不提的技术点那就是 intrinsic，这来源于一道面试题：为什么 String 类的 indexOf 方法，比我们使用相同代码实现的方法，执行效率要高得多？</p>
<p>在翻看 JDK 的源码时，能够看到很多地方使用了 <strong>HotSpotIntrinsicCandidate</strong> 注解。比如 StringBuffer 的 append 方法：</p>
<pre><code> @Override
@HotSpotIntrinsicCandidate
public synchronized StringBuffer append(char c) {
        toStringCache = null;
        super.append(c);
        return this;
}
</code></pre>
<p>被 @HotSpotIntrinsicCandidate 标注的方法，在 HotSpot 中都有一套高效的实现，该高效实现基于 CPU 指令，运行时，HotSpot 维护的高效实现会替代 JDK 的源码实现，从而获得更高的效率。</p>
<p>上面的问题中，我们往下跟踪实现，可以发现 StringLatin1 类中的 indexOf 方法，同样适用了 HotSpotIntrinsicCandidate 注解，原因也就在于此。</p>
<pre><code>@HotSpotIntrinsicCandidate
    public static int indexOf(byte[] value, byte[] str) {
        if (str.length == 0) {
            return 0;
        }
        if (value.length == 0) {
            return -1;
        }
        return indexOf(value, value.length, str, str.length, 0);
    }

    @HotSpotIntrinsicCandidate
    public static int indexOf(byte[] value, int valueCount, byte[] str, int strCount, int fromIndex) {
        byte first = str[0];
</code></pre>
<p><img src="assets/Ciqah157A7yAHKkqAADmapAcCaE181.jpg" alt="img" /></p>
<p>JDK 中这种方法有接近 400 个，可以在 IDEA 中使用 <strong>Find Usages</strong> 找到它们。</p>
<h2>小结</h2>
<p>JIT 是现代 JVM 主要的优化点，能够显著地增加程序的执行效率，从解释执行到最高层次的 C2，一个数量级的性能提升也是有可能的。但即时编译的过程是非常缓慢的，耗时间也费空间，所以这些优化操作会和解释执行同时进行。</p>
<p>一般，方法首先会被解释执行，然后被 3 层的 C1 编译，最后被 4 层的 C2 编译，这个过程也不是一蹴而就的。</p>
<p>常用的优化手段，有公共子表达式消除、数组范围检查消除、方法内联、逃逸分析等。</p>
<p>其中，方法内联通过将短小精悍的代码融入到调用方法的执行逻辑里，来减少方法调用上的开支；逃逸分析通过分析变量的引用范围，对象可能会使用栈上分配的方式来减少 GC 的压力，或者使用标量替换来获取更多的优化。</p>
<p>这个过程的执行细节并不是那么“确定”，在不同的 JVM 中，甚至在不同的 HotSpot 版本中，效果也不尽相同。</p>
<p>使用 JITWatch 工具，能够看到字节码和机器码的对应关系，以及执行过程中的一系列优化操作。若想要了解这个工具的更多功能，<a href="https://github.com/AdoptOpenJDK/jitwatch/wiki">可以点击这里参考 wiki</a>。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="22&#32;深入剖析：如何使用&#32;Java&#32;Agent&#32;技术对字节码进行修改.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="24&#32;案例分析：大型项目如何进行性能瓶颈调优？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4358eebf1c645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
