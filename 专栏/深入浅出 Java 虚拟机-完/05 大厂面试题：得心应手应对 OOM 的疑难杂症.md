<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>05 大厂面试题：得心应手应对 OOM 的疑难杂症.md</title>
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

                    <a class="current-tab" href="05&#32;大厂面试题：得心应手应对&#32;OOM&#32;的疑难杂症.md">05 大厂面试题：得心应手应对 OOM 的疑难杂症.md</a>
                    

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
                        <div><h1>05 大厂面试题：得心应手应对 OOM 的疑难杂症</h1>
<p>在前面几个课时中，我们不止一次提到了堆（heap），堆是一个巨大的对象池。在这个对象池中管理着数量巨大的对象实例。</p>
<p>而池中对象的引用层次，有的是很深的。一个被频繁调用的接口，每秒生成对象的速度，也是非常可观的。对象之间的关系，形成了一张巨大的网。虽然 Java 一直在营造一种无限内存的氛围，但对象不能只增不减，所以需要垃圾回收。</p>
<p>那 JVM 是如何判断哪些对象应该被回收？哪些应该被保持呢？</p>
<p>在古代，刑罚中有诛九族一说。指的是有些人犯大事时，皇上杀一人不足以平复内心的愤怒时，会对亲朋好友产生连带责任。诛九族时首先需要追溯到一个共同的祖先，再往下细数连坐。堆上的垃圾回收也有同样的思路。我们接下来就具体分析 JVM 中是如何进行垃圾回收的。</p>
<p>JVM 的 GC 动作，是不受程序控制的，它会在满足条件的时候，自动触发。</p>
<p>在发生 GC 的时候，一个对象，JVM 总能够找到引用它的祖先。找到最后，如果发现这个祖先已经名存实亡了，它们都会被清理掉。而能够躲过垃圾回收的那些祖先，比较特殊，它们的名字就叫作 GC Roots。</p>
<p>从 GC Roots 向下追溯、搜索，会产生一个叫作 Reference Chain 的链条。当一个对象不能和任何一个 GC Root 产生关系时，就会被无情的诛杀掉。</p>
<p>如图所示，Obj5、Obj6、Obj7，由于不能和 GC Root 产生关联，发生 GC 时，就会被摧毁。</p>
<p><img src="assets/CgpOIF4heVuAPrWVAACK3qrA9-0011.png" alt="img" /></p>
<p>垃圾回收就是围绕着 GC Roots 去做的。同时，它也是很多内存泄露的根源，因为其他引用根本没有这样的权利。</p>
<p>那么，什么样的对象，才会是 GC Root 呢？这不在于它是什么样的对象，而在于它所处的位置。</p>
<h3>GC Roots 有哪些</h3>
<p>GC Roots 是一组必须活跃的引用。用通俗的话来说，就是程序接下来通过直接引用或者间接引用，能够访问到的潜在被使用的对象。</p>
<p>GC Roots 包括：</p>
<ul>
<li>Java 线程中，当前所有正在被调用的方法的引用类型参数、局部变量、临时值等。也就是与我们栈帧相关的各种引用。</li>
<li>所有当前被加载的 Java 类。</li>
<li>Java 类的引用类型静态变量。</li>
<li>运行时常量池里的引用类型常量（String 或 Class 类型）。</li>
<li>JVM 内部数据结构的一些引用，比如 sun.jvm.hotspot.memory.Universe 类。</li>
<li>用于同步的监控对象，比如调用了对象的 wait() 方法。</li>
<li>JNI handles，包括 global handles 和 local handles。</li>
</ul>
<p>这些 GC Roots 大体可以分为三大类，下面这种说法更加好记一些：</p>
<ul>
<li>活动线程相关的各种引用。</li>
<li>类的静态变量的引用。</li>
<li>JNI 引用。</li>
</ul>
<p><img src="assets/Cgq2xl4hefWAWKFZAAMwndGjScg437.png" alt="img" /></p>
<p>有两个注意点：</p>
<ul>
<li>我们这里说的是活跃的引用，而不是对象，对象是不能作为 GC Roots 的。</li>
<li>GC 过程是找出所有活对象，并把其余空间认定为“无用”；而不是找出所有死掉的对象，并回收它们占用的空间。所以，哪怕 JVM 的堆非常的大，基于 tracing 的 GC 方式，回收速度也会非常快。</li>
</ul>
<h3>引用级别</h3>
<p>接下来的一道面试题就有意思多了：能够找到 Reference Chain 的对象，就一定会存活么？</p>
<p>我在面试的时候，经常会问这些问题，比如“弱引用有什么用处”？令我感到奇怪的是，即使是一些工作多年的 Java 工程师，对待这个问题也是一知半解，错失了很多机会。</p>
<p>对象对于另外一个对象的引用，要看关系牢靠不牢靠，可能在链条的其中一环，就断掉了。</p>
<p><img src="assets/Cgq2xl4hehyAEx1JAABb83OQ5S0469.png" alt="img" /></p>
<p>根据发生 GC 时，这条链条的表现，可以对这个引用关系进行更加细致的划分。</p>
<p>它们的关系，可以分为强引用、软引用、弱引用、虚引用等。</p>
<h4>强引用 Strong references</h4>
<p>当内存空间不足，系统撑不住了，JVM 就会抛出 OutOfMemoryError 错误。即使程序会异常终止，这种对象也不会被回收。这种引用属于最普通最强硬的一种存在，只有在和 GC Roots 断绝关系时，才会被消灭掉。</p>
<p>这种引用，你每天的编码都在用。例如：new 一个普通的对象。</p>
<pre><code class="language-java">Object obj = new Object()
</code></pre>
<p>这种方式可能是有问题的。假如你的系统被大量用户（User）访问，你需要记录这个 User 访问的时间。可惜的是，User 对象里并没有这个字段，所以我们决定将这些信息额外开辟一个空间进行存放。</p>
<pre><code class="language-java">static Map&lt;User,Long&gt; userVisitMap = new HashMap&lt;&gt;();

...

userVisitMap.put(user, time);
</code></pre>
<p>当你用完了 User 对象，其实你是期望它被回收掉的。但是，由于它被 userVisitMap 引用，我们没有其他手段 remove 掉它。这个时候，就发生了内存泄漏（memory leak）。</p>
<p>这种情况还通常发生在一个没有设定上限的 Cache 系统，由于设置了不正确的引用方式，加上不正确的容量，很容易造成 OOM。</p>
<h4>软引用 Soft references</h4>
<p>软引用用于维护一些可有可无的对象。在内存足够的时候，软引用对象不会被回收，只有在内存不足时，系统则会回收软引用对象，如果回收了软引用对象之后仍然没有足够的内存，才会抛出内存溢出异常。</p>
<p>可以看到，这种特性非常适合用在缓存技术上。比如网页缓存、图片缓存等。</p>
<p>Guava 的 CacheBuilder，就提供了软引用和弱引用的设置方式。在这种场景中，软引用比强引用安全的多。</p>
<p>软引用可以和一个引用队列（ReferenceQueue）联合使用，如果软引用所引用的对象被垃圾回收，Java 虚拟机就会把这个软引用加入到与之关联的引用队列中。</p>
<p>我们可以看一下它的代码。软引用需要显式的声明，使用泛型来实现。</p>
<pre><code class="language-java">// 伪代码

Object object = new Object();

SoftReference&lt;Object&gt; softRef = new SoftReference(object);
</code></pre>
<p>这里有一个相关的 JVM 参数。它的意思是：每 MB 堆空闲空间中 SoftReference 的存活时间。这个值的默认时间是1秒（1000）。</p>
<pre><code class="language-java">-XX:SoftRefLRUPolicyMSPerMB=&lt;N&gt;
</code></pre>
<p>这里要特别说明的是，网络上一些流传的优化方法，即把这个值设置成 0，其实是错误的，这样容易引发故障，感兴趣的话你可以自行搜索一下。</p>
<p>这种比较偏门的优化手段，除非在你对其原理相当了解的情况下，才能设置一些比较特殊的值。比如 0 值，无限大等，这种值在 JVM 的设置中，最好不要发生。</p>
<h4>弱引用 Weak references</h4>
<p>弱引用对象相比较软引用，要更加无用一些，它拥有更短的生命周期。</p>
<p>当 JVM 进行垃圾回收时，无论内存是否充足，都会回收被弱引用关联的对象。弱引用拥有更短的生命周期，在 Java 中，用 java.lang.ref.WeakReference 类来表示。</p>
<p>它的应用场景和软引用类似，可以在一些对内存更加敏感的系统里采用。它的使用方式类似于这段的代码：</p>
<pre><code class="language-java">// 伪代码

Object object = new Object();

WeakReference&lt;Object&gt; softRef = new WeakReference(object);
</code></pre>
<h4>虚引用 Phantom References</h4>
<p>这是一种形同虚设的引用，在现实场景中用的不是很多。虚引用必须和引用队列（ReferenceQueue）联合使用。如果一个对象仅持有虚引用，那么它就和没有任何引用一样，在任何时候都可能被垃圾回收。</p>
<p>实际上，虚引用的 get，总是返回 null。</p>
<pre><code class="language-java">Object  object = new Object();

ReferenceQueue queue = new ReferenceQueue();

// 虚引用，必须与一个引用队列关联

PhantomReference pr = new PhantomReference(object, queue);
</code></pre>
<p>虚引用主要用来跟踪对象被垃圾回收的活动。</p>
<p>当垃圾回收器准备回收一个对象时，如果发现它还有虚引用，就会在回收对象之前，把这个虚引用加入到与之关联的引用队列中。</p>
<p>程序如果发现某个虚引用已经被加入到引用队列，那么就可以在所引用的对象的内存被回收之前采取必要的行动。</p>
<p>下面的方法，就是一个用于监控 GC 发生的例子。</p>
<pre><code class="language-java">private static void startMonitoring(ReferenceQueue&lt;MyObject&gt; referenceQueue, Reference&lt;MyObject&gt; ref) {

     ExecutorService ex = Executors.newSingleThreadExecutor();

     ex.execute(() -&gt; {

         while (referenceQueue.poll()!=ref) {

             //don't hang forever

             if(finishFlag){

                 break;

            }

        }

         System.out.println(&quot;-- ref gc'ed --&quot;);

    });

     ex.shutdown();

}
</code></pre>
<p>基于虚引用，有一个更加优雅的实现方式，那就是 Java 9 以后新加入的 Cleaner，用来替代 Object 类的 finalizer 方法。</p>
<h3>典型 OOM 场景</h3>
<p>OOM 的全称是 Out Of Memory，那我们的内存区域有哪些会发生 OOM 呢？我们可以从内存区域划分图上，看一下彩色部分。
<img src="assets/Cgq2xl4hepeAAwhWAAJfLYUzaPI499.png" alt="img" /></p>
<p>可以看到除了程序计数器，其他区域都有OOM溢出的可能。但是最常见的还是发生在堆上。
<img src="assets/Cgq2xl4heqWAZMlOAAA-Cqk2QcM143.png" alt="img" /></p>
<p>所以 OOM 到底是什么引起的呢？有几个原因：</p>
<ul>
<li>内存的容量太小了，需要扩容，或者需要调整堆的空间。</li>
<li>错误的引用方式，发生了内存泄漏。没有及时的切断与 GC Roots 的关系。比如线程池里的线程，在复用的情况下忘记清理 ThreadLocal 的内容。</li>
<li>接口没有进行范围校验，外部传参超出范围。比如数据库查询时的每页条数等。</li>
<li>对堆外内存无限制的使用。这种情况一旦发生更加严重，会造成操作系统内存耗尽。</li>
</ul>
<p>典型的内存泄漏场景，原因在于对象没有及时的释放自己的引用。比如一个局部变量，被外部的静态集合引用。</p>
<p><img src="assets/Cgq2xl4hesWATlosAAJxxYIdMjs057.png" alt="img" /></p>
<p>你在平常写代码时，一定要注意这种情况，千万不要为了方便把对象到处引用。即使引用了，也要在合适时机进行手动清理。关于这部分的问题根源排查，我们将在实践课程中详细介绍。</p>
<h3>小结</h3>
<p>你可以注意到 GC Roots 的专业叫法，就是可达性分析法。另外，还有一种叫作引用计数法的方式，在判断对象的存活问题上，经常被提及。</p>
<p>因为有循环依赖的硬伤，现在主流的 JVM，没有一个是采用引用计数法来实现 GC 的，所以我们大体了解一下就可以。引用计数法是在对象头里维护一个 counter 计数器，被引用一次数量 +1，引用失效记数 -1。计数器为 0 时，就被认为无效。你现在可以忘掉引用计数的方式了。</p>
<p>本课时，我们详细介绍了 GC Roots 都包含哪些内容。HostSpot 采用 tracing 的方式进行 GC，内存回收的速度与处于 living 状态的对象数量有关。</p>
<p>这部分涉及的内容较多，如果面试被问到，你可以采用白话版的方式进行介绍，然后举例深入。</p>
<p>接下来，我们了解到四种不同强度的引用类型，尤其是软引用和虚引用，在平常工作中使用还是比较多的。这里面最不常用的就是虚引用，但是它引申出来的 Cleaner 类，是用来替代 finalizer 方法的，这是一个比较重要的知识点。</p>
<p>本课时最后讨论了几种典型的 OOM 场景，你可能现在对其概念比较模糊。接下来的课时，我们将详细介绍几个常见的垃圾回收算法，然后对这些 OOM 的场景逐个击破。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="04&#32;动手实践：从栈帧看字节码是如何在&#32;JVM&#32;中进行流转的.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="06&#32;深入剖析：垃圾回收你真的了解吗？（上）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43588f6927645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
