<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>18  高级进阶：JIT 如何影响 JVM 的性能？.md</title>
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

                    
                    <a href="00&#32;Java&#32;性能优化，是进阶高级架构师的炼金石.md">00 Java 性能优化，是进阶高级架构师的炼金石.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;理论分析：性能优化，有哪些衡量指标？需要注意什么？.md">01 理论分析：性能优化，有哪些衡量指标？需要注意什么？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;理论分析：性能优化有章可循，谈谈常用的切入点.md">02 理论分析：性能优化有章可循，谈谈常用的切入点.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;深入剖析：哪些资源，容易成为瓶颈？.md">03 深入剖析：哪些资源，容易成为瓶颈？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;工具实践：如何获取代码性能数据？.md">04 工具实践：如何获取代码性能数据？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;工具实践：基准测试&#32;JMH，精确测量方法性能.md">05 工具实践：基准测试 JMH，精确测量方法性能.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;案例分析：缓冲区如何让代码加速.md">06 案例分析：缓冲区如何让代码加速.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;案例分析：无处不在的缓存，高并发系统的法宝.md">07  案例分析：无处不在的缓存，高并发系统的法宝.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;案例分析：Redis&#32;如何助力秒杀业务.md">08  案例分析：Redis 如何助力秒杀业务.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;案例分析：池化对象的应用场景.md">09  案例分析：池化对象的应用场景.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;案例分析：大对象复用的目标和注意点.md">10  案例分析：大对象复用的目标和注意点.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;案例分析：如何用设计模式优化性能.md">11  案例分析：如何用设计模式优化性能.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;案例分析：并行计算让代码“飞”起来.md">12  案例分析：并行计算让代码“飞”起来.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;案例分析：多线程锁的优化.md">13  案例分析：多线程锁的优化.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;案例分析：乐观锁和无锁.md">14  案例分析：乐观锁和无锁.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;案例分析：从&#32;BIO&#32;到&#32;NIO，再到&#32;AIO.md">15  案例分析：从 BIO 到 NIO，再到 AIO.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;案例分析：常见&#32;Java&#32;代码优化法则.md">16  案例分析：常见 Java 代码优化法则.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;高级进阶：JVM&#32;如何完成垃圾回收？.md">17  高级进阶：JVM 如何完成垃圾回收？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="18&#32;&#32;高级进阶：JIT&#32;如何影响&#32;JVM&#32;的性能？.md">18  高级进阶：JIT 如何影响 JVM 的性能？.md</a>
                    

                </li>
                <li>

                    
                    <a href="19&#32;&#32;高级进阶：JVM&#32;常见优化参数.md">19  高级进阶：JVM 常见优化参数.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;SpringBoot&#32;服务性能优化.md">20  SpringBoot 服务性能优化.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;性能优化的过程方法与求职面经总结.md">21  性能优化的过程方法与求职面经总结.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;结束语&#32;&#32;实践出真知.md">22 结束语  实践出真知.md</a>

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
                        <div><h1>18  高级进阶：JIT 如何影响 JVM 的性能？</h1>
<p>我们在上一课时，我们了解到 Java 虚拟机栈，其实是一个双层的栈，如下图所示，第一层就是针对 method 的栈帧，第二层是针对字节码指令的操作数栈。</p>
<p><img src="assets/CgqCHl9YevCARjawAAC9Bvf_IoE321.png" alt="Drawing 0.png" /></p>
<p>Java 虚拟机栈图</p>
<p>栈帧的创建是需要耗费资源的，尤其是对于 Java 中常见的 getter、setter 方法来说，这些代码通常只有一行，每次都创建栈帧的话就太浪费了。</p>
<p>另外，Java 虚拟机栈对代码的执行，采用的是字节码解释的方式，考虑到下面这段代码，变量 a 声明之后，就再也不被使用，要是按照字节码指令解释执行的话，就要做很多无用功。</p>
<pre><code>public class A{
    int attr = 0;
    public void test(){
        int a = attr;
        System.out.println(&quot;ok&quot;);
    }
}
</code></pre>
<p>下面是这段代码的字节码指令，我们能够看到 aload_0，getfield ，istore_1 这三个无用的字节码指令操作。</p>
<pre><code> public void test();
    descriptor: ()V
    flags: ACC_PUBLIC
    Code:
      stack=2, locals=2, args_size=1
         0: aload_0
         1: getfield      #2                  // Field attr:I
         4: istore_1
         5: getstatic     #3                  // Field java/lang/System.out:Ljava/io/PrintStream;
         8: ldc           #4                  // String ok
        10: invokevirtual #5                  // Method java/io/PrintStream.println:(Ljava/lang/String;)V
        13: return
      LineNumberTable:
        line 4: 0
        line 5: 5
        line 6: 13
</code></pre>
<p>另外，我们了解到垃圾回收器回收的目标区域主要是堆，堆上创建的对象越多，GC 的压力就越大。要是能把一些变量，直接在栈上分配，那 GC 的压力就会小一些。</p>
<p>其实，我们说的这几个优化的可能性，JVM 已经通过 JIT 编译器（Just In Time Compiler）去做了，JIT 最主要的目标是把解释执行变成编译执行。</p>
<p>为了提高热点代码的执行效率，在运行时，虚拟机将会把这些代码编译成与本地平台相关的机器码，并进行各种层次的优化，这就是 JIT 编译器的功能。</p>
<p><img src="assets/CgqCHl9YeyCAWROAAABdUyAOP5E893.png" alt="Drawing 2.png" /></p>
<p>如上图，JVM 会将调用次数很高，或者在 for 循环里频繁被使用的代码，编译成机器码，然后缓存在 CodeCache 区域里，下次调用相同方法的时候，就可以直接使用。</p>
<p>那 JIT 编译都有哪些手段呢？接下来我们详细介绍。</p>
<h3>方法内联</h3>
<p>在 <strong>“05 | 工具实践：基准测试 JMH，精确测量方法性能”</strong> 提到 JMH 的时候，我们就了解到 CompilerControl 注解可以控制 JIT 编译器的一些行为。</p>
<p>其中，有一个模式叫作<strong>inline</strong>，就是内联的意思，它会把一些短小的方法体，直接纳入目标方法的作用范围之内，就像是直接在代码块中追加代码。这样，就少了一次方法调用，执行速度就能够得到提升，这就是方法内联的概念。</p>
<p>可以使用 -XX:-Inline 参数来禁用方法内联，如果想要更细粒度的控制，可以使用 CompileCommand 参数，例如：</p>
<pre><code>-XX:CompileCommand=exclude,java/lang/String.indexOf
</code></pre>
<p>JMH 就是使用这个参数来实现的自定义编译特性。
在 JDK 的源码里，也有很多被 <strong>@ForceInline</strong>注解的方法，这些方法，会在执行的时候被强制进行内联；而被**@DontInline**注解的方法，则始终不会被内联。</p>
<p>我们从 <strong>“05 | 工具实践：基准测试 JMH，精确测量方法性能”</strong> 获取第 16 个代码示例，来看一下 JIT 这些优化的效果，主要代码块如下：</p>
<pre><code>public void target_blank() {
    // this method was intentionally left blank
}

@CompilerControl(CompilerControl.Mode.DONT_INLINE)
public void target_dontInline() {
    // this method was intentionally left blank
}

@CompilerControl(CompilerControl.Mode.INLINE)
public void target_inline() {
    // this method was intentionally left blank
}

@CompilerControl(CompilerControl.Mode.EXCLUDE)
public void target_exclude() {
    // this method was intentionally left blank
}
</code></pre>
<p>执行结果如下，可以看到不使用 JIT 编译和使用了 JIT 编译的性能差距达到了 100 多倍，使用了内联比不使用内联，速度快了 5 倍。</p>
<pre><code>Benchmark                                Mode  Cnt   Score   Error  Units
JMHSample_16_CompilerControl.baseline    avgt    3   0.485 ± 1.492  ns/op
JMHSample_16_CompilerControl.blank       avgt    3   0.483 ± 1.518  ns/op
JMHSample_16_CompilerControl.dontinline  avgt    3   1.934 ± 3.112  ns/op
JMHSample_16_CompilerControl.exclude     avgt    3  57.603 ± 4.435  ns/op
JMHSample_16_CompilerControl.inline      avgt    3   0.483 ± 1.520  ns/op
</code></pre>
<p><img src="assets/CgqCHl9Ye0KASdaPAAFd8UGlCRY151.png" alt="Drawing 4.png" /></p>
<p>JIT 编译之后的二进制代码，是放在 Code Cache 区域里的。这个区域的大小是固定的，而且一旦启动无法扩容。如果 Code Cache 满了，JVM 并不会报错，但会停止编译。所以编译执行就会退化为解释执行，性能就会降低。不仅如此，JIT 编译器会一直尝试去优化你的代码，造成 CPU 占用上升。</p>
<p>通过参数 -XX:ReservedCodeCacheSize 可以指定 Code Cache 区域的大小，如果你通过监控发现空间达到了上限，就要适当的增加它的大小。</p>
<h3>编译层次</h3>
<p>HotSpot 虚拟机包含多个即时编译器，有 C1，C2 和 Graal，JDK8 以后采用的是分层编译的模式。使用 jstack 命令获得的线程信息，经常能看到它们的身影。</p>
<pre><code>&quot;C2 CompilerThread0&quot; #6 daemon prio=9 os_prio=31 cpu=830.41ms elapsed=4252.14s tid=0x00007ffaed023000 nid=0x5a03 waiting on condition  [0x0000000000000000]
   java.lang.Thread.State: RUNNABLE
   No compile task

&quot;C1 CompilerThread0&quot; #8 daemon prio=9 os_prio=31 cpu=549.91ms elapsed=4252.14s tid=0x00007ffaed831800 nid=0x5c03 waiting on condition  [0x0000000000000000]
   java.lang.Thread.State: RUNNABLE
   No compile task
</code></pre>
<p>使用额外线程进行即时编译，可以不用阻塞解释执行的逻辑。JIT 通常会在触发之后就在后台运行，编译完成之后就将相应的字节码替换为编译后的代码。
JIT 编译方式有两种：一种是编译方法，另一种是编译循环。</p>
<p>分层编译将 Java 虚拟机的执行状态分为了五个层次。</p>
<ul>
<li>字节码的解释执行;</li>
<li>执行不带 profiling 的 C1 代码;</li>
<li>执行仅带方法调用次数以及循环执行次数 profiling 的 C1 代码;</li>
<li>执行带所有 profiling 的 C1 代码;</li>
<li>执行 C2 代码。</li>
</ul>
<p>其中，Profiling 指的是运行时的程序的执行状态数据，比如循环调用的次数、方法调用的次数、分支跳转次数、类型转换次数等。比如 JDK 中的 hprof 工具，就是一种 profiler，说白了就是一些中间的统计数据。</p>
<p>在不启用分层编译的情况下，当方法的调用次数和循环回边的次数的总和，超过由参数 -XX:CompileThreshold 指定的阈值时，便会触发即时编译；但当启用分层编译时，这个参数将会失效，会采用一套动态调整进行调整。</p>
<h3>逃逸分析</h3>
<p><strong>下面着重讲解一下逃逸分析，这个知识点在面试的时候经常会被问到。</strong></p>
<p>我们先回顾一下上一课时留下的问题：我们常说的对象，除了基本数据类型，一定是在堆上分配的吗？</p>
<p>答案是否定的，通过逃逸分析，JVM 能够分析出一个新的对象的使用范围，从而决定是否要将这个对象分配到堆上。逃逸分析现在是 JVM 的默认行为，可以通过参数 -XX:-DoEscapeAnalysis 关掉它。</p>
<p>那什么样的对象算是逃逸的呢？可以看一下下面的两种典型情况。</p>
<p>如代码所示，对象被赋值给成员变量或者静态变量，可能被外部使用，变量就发生了逃逸。</p>
<pre><code>public class EscapeAttr {
    Object attr;
    public void test() {
        attr = new Object();
    }
}
</code></pre>
<p>再看下面这段代码，对象通过 return 语句返回。由于程序并不能确定这个对象后续会不会被使用，外部的线程能够访问到这个结果，对象也发生了逃逸。</p>
<pre><code>public class EscapeReturn {
    Object attr;
    public Object test() {
        Object obj = new Object();
        return obj;
    }
}
</code></pre>
<p>那逃逸分析有什么好处呢？
<strong>1. 栈上分配</strong></p>
<p>如果一个对象在子程序中被分配，指向该对象的指针永远不会逃逸，对象有可能会被优化为栈分配。栈分配可以快速地在栈帧上创建和销毁对象，不用再分配到堆空间，可以有效地减少 GC 的压力。</p>
<p><strong>2. 分离对象或标量替换</strong></p>
<p>但对象结构通常都比较复杂，如何将对象保存在栈上呢？</p>
<p>JIT 可以将对象打散，全部替换为一个个小的局部变量，这个打散的过程，就叫作标量替换（标量就是不能被进一步分割的变量，比如 int、long 等基本类型）。也就是说，标量替换后的对象，全部变成了局部变量，可以方便地进行栈上分配，而无须改动其他的代码。</p>
<p>从上面的描述我们可以看到，并不是所有的对象或者数组，都会在堆上分配。由于JIT的存在，如果发现某些对象没有逃逸出方法，那么就有可能被优化成栈分配。</p>
<p><strong>3.同步消除</strong></p>
<p>如果一个对象被发现只能从一个线程被访问到，那么对于这个对象的操作可以不考虑同步。</p>
<p>注意这是针对 synchronized 来说的，JUC 中的 Lock 并不能被消除。</p>
<p>要开启同步消除，需要加上 -XX:+EliminateLocks 参数。由于这个参数依赖逃逸分析，所以同时要打开 -XX:+DoEscapeAnalysis 选项。</p>
<p>比如下面这段代码，JIT 判断对象锁只能被一个线程访问，就可以去掉这个同步的影响。</p>
<pre><code>public class SyncEliminate {
    public void test() {
        synchronized (new Object()) {
        }
    }
}
</code></pre>
<p>仓库中也有一个 StringBuffer 和 StringBuilder 的 JMH 测试对比，可以看到在开启了锁消除的情况下，它们的效率相差并不大。</p>
<pre><code>Benchmark                          Mode  Cnt       Score       Error   Units
BuilderVsBufferBenchmark.buffer   thrpt   10   90085.927 ± 95174.289  ops/ms
BuilderVsBufferBenchmark.builder  thrpt   10  103280.200 ± 76172.538  ops/ms
</code></pre>
<h3>JITWatch</h3>
<p>可以使用 jitwatch 工具来观测 JIT 的一些行为。</p>
<pre><code>https://github.com/AdoptOpenJDK/jitwatch
</code></pre>
<p>在代码的启动参数里加入 LogCompilation 等参数开启记录，将生成一个 jitdemo.log 文件。</p>
<pre><code> -XX:+UnlockDiagnosticVMOptions -XX:+TraceClassLoading  -XX:+PrintAssembly -XX:+LogCompilation -XX:LogFile=jitdemo.log
</code></pre>
<p>使用 jitwatch 工具，可打开这个文件，看到详细的编译结果。</p>
<p><img src="assets/Ciqc1F9Ye36AMYIDAAcn4iSavAY997.png" alt="Drawing 5.png" /></p>
<p>下面是一段测试代码：</p>
<pre><code>public class SimpleInliningTest {
    public SimpleInliningTest() {
        int sum = 0;
        // 1_000_000 is F4240 in hex
        for (int i = 0; i &lt; 1_000_000; i++) {
            sum = this.add(sum, 99);
            // 63 hex
        }
        System.out.println(&quot;Sum:&quot; + sum);
    }

    public int add(int a, int b) {
        return a + b;
    }
    public static void main(String[] args) {
        new SimpleInliningTest();
    }
}
</code></pre>
<p>从执行后的结果可以看到，热点 for 循环已经使用 JIT 进行了编译，而里面应用的 add 方法，也已经被内联。</p>
<p><img src="assets/CgqCHl9Ye4eAaVmXAATwlN8rh4w940.png" alt="Drawing 6.png" /></p>
<h3>小结</h3>
<p>JIT 是现代 JVM 主要的优化点，能够显著地提升程序的执行效率。从解释执行到最高层次的 C2，一个数量级的性能提升也是有可能的。但即时编译的过程是非常缓慢的，既耗时间也费空间，所以这些优化操作会和解释执行同时进行。</p>
<p>值得注意的是，JIT 在某些情况下还会出现逆优化。比如一些热部署方式触发的 redefineClass，就会造成 JIT 编译结果的失效，相关的内联代码也需要重新生成。</p>
<p>JIT 优化并不见得每次都有用，比如下面这段代码，编译后执行，会发生死循环。但如果你在启动的时候，加上 <strong>-Djava.compiler=NONE</strong> 参数，禁用 JIT，它就能够执行下去。</p>
<pre><code>public class Demo {
	static final class TestThread extends Thread {
		boolean stop = false;
		public boolean isStop() {
			return stop;
		}
		@Override
		public void run() {
			try {
				Thread.sleep(100);
			} catch (Exception ex) {
				ex.printStackTrace();
			}
			stop = true;
			System.out.println(&quot;END&quot;);
		}
	}
	public static void main(String[] args) {
		int i = 0;
		TestThread test = new TestThread();
		test.start();
		while(!test.isStop()){
			System.out.println(&quot;--&quot;);
			i++;
		}
	}
}
</code></pre>
<p><strong>我们主要看了方法内联、逃逸分析等概念，了解到一些方法在被优化后，对象并不一定是在堆上分配的，它可能在被标量替换后，直接在栈上分配。这几个知识点也是在面试中经常被问到的。</strong></p>
<p>JIT 的这些优化一般都是在后台进程默默地去做了，我们不需要关注太多。Code Cache 的容量达到上限，会影响程序执行的效率，但除非你有特别多的代码，默认的 240M 一般来说，足够用了。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="17&#32;&#32;高级进阶：JVM&#32;如何完成垃圾回收？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="19&#32;&#32;高级进阶：JVM&#32;常见优化参数.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43438b5ceb70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Java%20%E6%80%A7%E8%83%BD%E4%BC%98%E5%8C%96%E5%AE%9E%E6%88%98-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
