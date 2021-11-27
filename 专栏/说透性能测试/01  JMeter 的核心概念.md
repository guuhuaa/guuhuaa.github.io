<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>01  JMeter 的核心概念.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;为什么每个测试人都要学好性能测试？.md">00 开篇词  为什么每个测试人都要学好性能测试？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="01&#32;&#32;JMeter&#32;的核心概念.md">01  JMeter 的核心概念.md</a>
                    

                </li>
                <li>

                    
                    <a href="02&#32;&#32;JMeter&#32;参数化策略.md">02  JMeter 参数化策略.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;构建并执行&#32;JMeter&#32;脚本的正确姿势.md">03  构建并执行 JMeter 脚本的正确姿势.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;JMeter&#32;二次开发其实并不难.md">04  JMeter 二次开发其实并不难.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;如何基于&#32;JMeter&#32;API&#32;开发性能测试平台？.md">05  如何基于 JMeter API 开发性能测试平台？.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;Nginx&#32;在系统架构中的作用.md">06  Nginx 在系统架构中的作用.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;你真的知道如何制定性能测试的目标吗？.md">07  你真的知道如何制定性能测试的目标吗？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;性能测试场景的分类和意义.md">08  性能测试场景的分类和意义.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;如何制定一份有效的性能测试方案？.md">09  如何制定一份有效的性能测试方案？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;命令行监控&#32;Linux&#32;服务器的要点.md">10  命令行监控 Linux 服务器的要点.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;分布式服务链路监控以及报警方案.md">11  分布式服务链路监控以及报警方案.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;如何把可视化监控也做得酷炫？.md">12  如何把可视化监控也做得酷炫？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;Docker&#32;的制作、运行以及监控.md">13  Docker 的制作、运行以及监控.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;如何从&#32;CPU&#32;飙升定位到热点方法？.md">14  如何从 CPU 飙升定位到热点方法？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;如何基于&#32;JVM&#32;分析内存使用对象？.md">15  如何基于 JVM 分析内存使用对象？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;如何通过&#32;Arthas&#32;定位代码链路问题？.md">16  如何通过 Arthas 定位代码链路问题？.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;如何应对&#32;Redis&#32;缓存穿透、击穿和雪崩？.md">17  如何应对 Redis 缓存穿透、击穿和雪崩？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;如何才能优化&#32;MySQL&#32;性能？.md">18  如何才能优化 MySQL 性能？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;如何根治慢&#32;SQL？.md">19  如何根治慢 SQL？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;结束语&#32;&#32;线上全链路性能测试实践总结.md">20 结束语  线上全链路性能测试实践总结.md</a>

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
                        <div><h1>01  JMeter 的核心概念</h1>
<p>从今天开始，我们将进入模块一的学习，在学习的过程中，希望你能够明白为什么 JMeter 要这么用并掌握 JMeter 的一些进阶用法。这一讲作为我们学习的第一讲，我将带你了解 JMeter 的核心概念，完善你对测试工具的认识。</p>
<h3>为什么是 JMeter</h3>
<p>性能测试有很多工具，JMeter、Loadrunner、Locust、nGrinder 都不乏粉丝。有人认为做性能测试重要的不是工具，是思想。但从学习实践的角度讲，工具在一定程度上决定了工作效率及协作模式。要成为一名测试专家，对工具一定是要精通的。</p>
<p>JMeter 原生的方式只支持单点工作，团队成员并不能很方便地互相检查脚本和查看报告。如果我们想改变这样的协作方式，就要对 JMeter 进行改造。如果不了解工具，改造也就无从谈起。</p>
<p>说了这么多，那我为什么会选择介绍 JMeter 呢？总的来说，它有以下 3 点优势。</p>
<ul>
<li><strong>开源免费、安装简易、多系统兼容</strong>。相对于 Loadrunner，JMeter 没有版权的困扰，脚本可以在 Windows、Linux、Mac 任意系统间切换，非常简单方便。</li>
<li><strong>丰富的基础插件</strong>。相对于 Locust，JMeter 提供了较多的插件，可以减少重复造轮子的工作。Locust 的基础功能需要写代码实现，更适合定制性较强的测试场景，如游戏类测试，在敏捷化的测试团队中需要考虑到这部分的时间成本问题。</li>
<li><strong>良好的拓展性</strong>。虽然 JMeter 已经有了丰富的基础插件，它本身还是提供了入口进行二次开发，以满足团队定制化的需求。同样，你也可以将 JMeter 平台化，通过平台化的操作来管理 JMeter，增强测试团队的协作性。</li>
</ul>
<p>我们虽然是从 JMeter 工具开始的，但网上其实已经提供了很多实例来教你 JMeter 的基础使用，所以这一讲的重点是帮你厘清 JMeter 设计上的一些核心理念。我将从 3 个方面来介绍，分别是：线程、循环、Ramp-Up，组件和元件，以及分布式压测。</p>
<p>我们先来看线程、循环、Ramp-Up。</p>
<h3>线程、循环、Ramp-Up</h3>
<p>这是你在 JMeter 的线程组元件中的线程属性，线程组建立是你使用 JMeter 进行性能测试最基础的步骤，压力发起策略几乎都依赖于这个元件。</p>
<h4>线程与循环</h4>
<p>我们先来看两张图，看看它们之间有什么区别。</p>
<p><img src="assets/Cip5yF_1Ha-ADn1PAABkFOXpDRg902.png" alt="Drawing 0.png" /></p>
<p>图 1：设置图 A</p>
<p><img src="assets/CgpVE1_1HbmATgMeAACJsBol0Mc903.png" alt="Drawing 1.png" /></p>
<p>图 2：设置图 B</p>
<p>从两张图的对比中，我们可以看到图 1 和图 2 的区别在于线程数和循环次数，一个是 1 和 10，一个则是 10 和 1。从结果来看，图 1 和图 2 都是发送了 10 个请求，那它们的核心区别是什么呢？ 我们不妨来看两段代码演示。</p>
<p>先来看图 1 的代码演示：</p>
<pre><code>for(int j=0;j&lt;10;j++) {

   System.out.println(Thread.currentThread().getName());//打印线程名字

}
</code></pre>
<p>这段代码我使用线程循环的方式打印运行线程的名字，运行后的内容如下：</p>
<pre><code>Thread-0

......

Thread-0

Thread-0 //可以看到是基于同一个线程
</code></pre>
<p>再来看图 2 的代码演示：</p>
<pre><code>for(int i=0;i&lt;10;i++){

    new Thread(new Runnable() {

        public void run() {

            System.out.println(Thread.currentThread().getName());

        }

    }).start();

} //示意代码
</code></pre>
<p>这段代码我是使用多线程的方式打印正在运行的线程，运行后效果如下：</p>
<pre><code>Thread-0

......

Thread-8

Thread-9 //不同的线程
</code></pre>
<p>以上代码内容主要是打印线程的名字。不难看出，循环的方式是基于同一个线程反复进行 10 次操作，而多线程则启动了 10 个不一样的线程，虽然都是向服务器发送了 10 次请求，但这两种方式完成的时间和对系统的压力也完全不一样。</p>
<p>打个比方，我们需要掰 100 斤玉米，一组是 10 个人一起掰，一组只有 1 个人掰，每个人的速度如果是一致的，不用想就知道哪个组更快。这样的场景经常发生在使用 JMeter 利用接口造数据时，同样是造 1 万条数据，如果你觉得速度很慢，那你就可以考虑一下多线程了。但掰玉米用 10 个人的成本当然要比用 1 个人来得多，我们的压力场景也是这样的。通常压力场景都是多线程的，线程的多少也直接决定了对被测系统压力的大小。</p>
<h4>Ramp-Up</h4>
<p>Ramp-Up 其实是一个可选项，如果没有特殊要求，保持默认配置脚本即可。如果填 1，代表在 1 秒内所有设置线程数全部启动。不过这个是理论上的，实际启动时间也依赖于硬件的接受程度。如果硬件跟不上，启动时间自然也会增加。</p>
<p>在有的性能测试场景中，如果你不想在性能测试一开始让服务器的压力过大，希望按照一定的速度增加线程到既定数值，你就可以使用这个选项。比如我想用 10 个线程进行测试，启动速度是每秒 2 个线程，就可以在这里填 5，如下所示：</p>
<p><img src="assets/Cip5yF_1HcyABzDxAABletIULYA933.png" alt="Drawing 2.png" /></p>
<p>图 3：设置图 C</p>
<p>我们来通过运行展示一下。</p>
<p><img src="assets/CgpVE1_1HdKAeBVLAAG5WhpVanI202.png" alt="Drawing 3.png" /></p>
<p>图 4：生成线程数</p>
<p>我使用了监听器中的用表格查看结果插件。通过这组数据可以看到，每秒产生了 2 个新的线程，合计在 5 秒内完成。</p>
<h3>组件和元件</h3>
<p>了解了线程、循环和 Ramp-Up，接着来聊聊组件和元件。</p>
<h4>组件和元件的关系</h4>
<p>要解释组件首先就要说元件。我们看图 4 中的 HTTP 请求，其实这就是一个实际的元件。同样作为元件的还可以是 JDBC 请求、Java 请求等，这一类元件我们统一称为取样器，也就是组件。我用一个示意图来表示组件和元件的关系：</p>
<p><img src="assets/CgqCHl_2gVaAEnd0AACHVOgTgLo426.png" alt="图片2.png" /></p>
<p>图 5：组件和元件关系图</p>
<p>如图所示，HTTP 请求、JDBC 请求等元件都从属于取样器。</p>
<h4>组件的作用</h4>
<p>JMeter 有多种组件，我们重点看下这七类： 配置元件、取样器、定时器、前置处理器、后置处理器、断言、监听器。我们来看下它们各自的作用。</p>
<ul>
<li><strong>配置元件</strong>：用于初始化变量，以便采样器使用。类似于框架的配置文件，参数化需要的配置都在配置元件中。</li>
<li><strong>取样器</strong>：承担 JMeter 发送请求的核心功能，支持多种请求类型，如 HTTP、FTP、JDBC 等，也可以使用 Java 类型的请求进行自定义编写。</li>
<li><strong>定时器</strong>：一般用来指定请求发送的延时策略。在没有定时器的情况下，JMeter 发送请求是不会暂停的。</li>
<li><strong>前置处理器</strong>：在进行取样器请求之前执行一些操作，比如生成入参数据。</li>
<li><strong>后置处理器</strong>：在取样器请求完成后执行一些操作，通常用于处理响应数据，从中提取需要的值。</li>
<li><strong>断言</strong>：主要用于判断取样器请求或对应的响应是否返回了期望的结果。</li>
<li><strong>监听器</strong>：监听器可以在 JMeter 执行测试的过程中搜集相关的数据，然后将这些数据在 JMeter 界面上以树、图、报告等形式呈现出来。不过图形化的呈现非常消耗客户端性能，在正式性能测试中并不推荐使用。</li>
</ul>
<h4>组件的顺序</h4>
<p>了解正确的组件执行顺序可以帮助你明白在什么情况下应该添加什么组件，而不会添加错误的组件造成不必要的麻烦。我将它们做了一个排序，如下图所示：</p>
<p><img src="assets/CgqCHl_2gWOAcj4PAADsoHDndjA019.png" alt="图片1.png" /></p>
<p>图 6：组件顺序</p>
<p>搞懂了组件顺序，你在测试前准备脚本生成参数化数据时，就可以在前置处理器中寻找相关元件；在要提取接口返回的数据，就可以在后置处理器中寻找相关插件，而不是在其他地方寻找数据，浪费时间。</p>
<p>我经常看到有的测试人员在需要在后置处理器中使用 BeanShell PostProcesor 的时候，错误地用了前置处理器中的 Beanshell PreProcessor，导致系统报错，无法实现预期的功能，甚至是测试无法进行下去。</p>
<h4>元件作用域</h4>
<p>以上说的都是组件相关的东西，这里就来看看元件作用域。我们先来看一张图：</p>
<p><img src="assets/Cip5yF_1He-ALsdzAACx-Dpj8Qo799.png" alt="Drawing 5.png" /></p>
<p>图 7：结果树 1、2、3</p>
<p>在图中可以看到，我在不同位置放了 3 个一样的元件“查看结果树”（为了方便区分，我分别标记了 1、2、3）。运行后发现，查看结果树 1（图 8）里面显示了 HTTP1 和 HTTP2，而插件结果树 2 里只有 HTTP1，查看结果树 3 里面只有 HTTP2。</p>
<p><img src="assets/CgpVE1_1HfyAP0epAAA7IET5M00253.png" alt="Drawing 6.png" /></p>
<p>图 8：查看结果树 1 的显示图</p>
<p>这是为什么呢？这就要说到元件作用域了。</p>
<p>通过截图可以发现 JMeter 元件除了从上到下的顺序外，有还具备一定的层次结构，比如图 5 中的响应断言和查看结果树，它相对于取样器存在父子组件的关系，说白了就是 HTTP 元件对取样器有效的区域，比如查看结果树 2 是 HTTP1 请求的子节点，那它就只对 HTTP1 生效；如果父节点是测试计划，那就会对测试计划下的 HTTP1 和 HTTP2 都生效。</p>
<h3>分布式压测</h3>
<p>压测就是 JMeter 通过产生大量线程对服务器进行访问产生负载，监听服务器返回结果并进行校验。在大部分情况下，用单台 JMeter 进行性能测试或者自动化测试是可行的，但在多线程运行过程中可能存在性能瓶颈，很多人在排查定位问题时经常会漏掉这一点。</p>
<p>从我的工作经验出发，单机的 JMeter 最好将线程数控制在 1000 以内；如果超过了 1000 线程，则建议使用 JMeter 分布式压测，这在一定程度上可以解决 JMeter 客户端自身形成的瓶颈问题。</p>
<p>在分布式 JMeter 架构下，JMeter 使用的是 Master 和 Slave。</p>
<h4>Master</h4>
<p>Master 负责远程控制 Slave（负载机）。分布式通常有多个 JMeter 节点，其中一个节点承担 Master 的作用。Master 通过发送信号控制节点机的启动和停止，并进行收集节点机的数据等操作。</p>
<h4>Slave</h4>
<p>Slave 一般也叫负载机，主要是发起线程来访问 target 服务器。一般在 Slave 节点机上先启动代理 jar 包，控制机远程连接，负载机运行脚本后对 Master 回传数据。流程示意图如下：</p>
<p><img src="assets/CgqCHl_2gXGAX4J2AAB_Vvcgr6E022.png" alt="图片3.png" /></p>
<p>图 9：Slave 流程示意图</p>
<p>JMeter 的 Master 和 Slave 配置也比较简单。将 JMeter 的 bin 目录下的 jmeter.properties 文件配置：IP 和 Port 是 Slave 机的 IP 以及默认的 1099 端口。如下所示：</p>
<pre><code>remote_hosts=ip:1099,ip:1099
</code></pre>
<p>Slave 启动 jar 包之后，默认会启动 1099 端口。Master 配置完成启动后便可以建立和 Slave 连接，从而进行控制和收集等操作。</p>
<p>一般来说，JMeter 分布式压测都是作为<strong>缓减</strong>客户端瓶颈的重要方式。这里我要强调“<strong>缓减</strong>”，因为在性能测试领域中不存在一种技术手段能够保证永远没有问题。随着公司的体量发展，对性能的要求也是水涨船高。JMeter 自带的分布式压测作为一种缓解客户端性能问题的方式，并不是万能法则。</p>
<h3>总结</h3>
<p>本讲我主要讲解了 JMeter 的核心设计理念，希望能够让你能对 JMeter 的核心概念有一定的理解。JMeter 作为目前最流行的性能测试工具，它本身提供的插件可以满足绝大多测试场景的使用，并且它也提供了二次开发的接口和 API，使用起来非常灵活。同时它分布式的使用方式也能够让你在较大程度上缓减客户端瓶颈。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="00&#32;开篇词&#32;&#32;为什么每个测试人都要学好性能测试？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="02&#32;&#32;JMeter&#32;参数化策略.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435b644dad645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E8%AF%B4%E9%80%8F%E6%80%A7%E8%83%BD%E6%B5%8B%E8%AF%95/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
