<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>05  如何基于 JMeter API 开发性能测试平台？.md</title>
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

                    
                    <a href="01&#32;&#32;JMeter&#32;的核心概念.md">01  JMeter 的核心概念.md</a>

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

                    <a class="current-tab" href="05&#32;&#32;如何基于&#32;JMeter&#32;API&#32;开发性能测试平台？.md">05  如何基于 JMeter API 开发性能测试平台？.md</a>
                    

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
                        <div><h1>05  如何基于 JMeter API 开发性能测试平台？</h1>
<p>上一讲我带你学习了 JMeter 二次开发，通过对 JMeter 提供的接口或者抽象类方法重写可以自定义所需要的 JMeter 插件。这一讲我将带你了解如何开发一个性能测试平台。</p>
<p>目前测试界比较热门的一个方向就是<strong>开发测试平台</strong>，平台级别的性能测试能减少重复劳动、提升效率，也方便统一管理，自然受到了市场的欢迎，测试平台开发能力也成了资深测试人员的必备技能之一。</p>
<p>本专栏，我们应用的主要性能测试工具是 JMeter，那开发性能测试平台需要什么样的能力呢？我认为需要以下能力：</p>
<ul>
<li><strong>具备较好的 Java 开发能力</strong>，JMeter 本身是 Java 开发，提供了较多的接口，所以使用 Java 开发具备天然的优势；</li>
<li>平台主要通过 Web 网页展示，需要具备较好的<strong>前端开发能力</strong>，目前 Vue 是比较流行的前端框架；</li>
<li><strong>熟悉 JMeter 源码结构</strong>，尤其是 JMeter 提供的相关 API。</li>
</ul>
<h3>构建性能测试平台的必要性</h3>
<p>为什么我会如此推荐你去开发性能测试平台呢？回想一下你在工作中是否遇到过以下场景：</p>
<ul>
<li>B 同学如果需要 A 同学写完的脚本，A 只能单独发给 B，如果 A 的脚本有变化，不能实时同步到 B，而且发送的过程也存在<strong>沟通成本和时间差</strong>；</li>
<li>测试执行后，需要将测试结果同步给开发者，很多测试都是手动截图，不仅方式原始而且还会存在<strong>信息缺失</strong>的情况；</li>
<li>结果追溯时，我们需要找一些历史数据却发现并没有<strong>存档或共享</strong>。</li>
</ul>
<p>这些场景使我们的性能测试平台具有了更多现实意义，我们希望有一个<strong>可以协作共享</strong>，并能够<strong>追溯历史数据的性能测试平台</strong>。基于这点我梳理了性能测试平台的基础功能，如下图所示：</p>
<p><img src="assets/Ciqc1GAFPJ-ASd02AAB5h9Xz8Ok173.png" alt="Drawing 0.png" /></p>
<p>图 1：性能测试平台基础功能</p>
<p>目前市面上的性能测试平台大多是基于 JMeter 提供的 API 开发的，核心流程如下图所示：</p>
<p><img src="assets/CgqCHmAFPKaACL8lAACO4B5j9fY519.png" alt="Drawing 1.png" /></p>
<p>图 2：性能测试平台开发核心流程</p>
<p>接下来我们根据这 4 个阶段来学习如何使用 JMeter 的 API 实现性能测试。</p>
<h3>环境初始化</h3>
<p>JMeter API 在执行过程中，首先会读取 JMeter 软件安装目录文件下配置文件里的属性，所以我们要通过 JMeter API 读取指定的 JMeter 主配置文件的目录以及 JMeter 的安装目录；此外，我们还需要初始化 JMeter API 运行的<strong>语言环境</strong>（默认是英语）和<strong>资源</strong>。以上便是 JMeter API 做初始化的目的。</p>
<p>其中环境初始化主要包括以下 2 个步骤：</p>
<ol>
<li>通过 JMeterUtils.loadJMeterProperties 加载安装目录的 JMeter 主配置文件 JMeter.properties，然后把 jmeter.properties 中的所有属性赋值给 JMeterUtils 对象，以便在脚本运行时可以获取所需的配置；</li>
<li>设置 JMeter 的安装目录，JMeter API 会根据我们指定的目录加载脚本运行时需要的配置，例如 saveservice.properties 配置文件中的所有配置。</li>
</ol>
<p>参考代码如下：</p>
<pre><code>JMeterUtils.loadJMeterProperties(&quot;C:/Program Files/JMeter/bin/jmeter.properties&quot;);

JMeterUtils.setJMeterHome(&quot;C:/Program Files/JMeter&quot;);

JMeterUtils.initLocale();
</code></pre>
<p>这样一来，我们就实现了环境初始化，代码中的目录可以根据自己实际的目录设置。</p>
<h3>脚本加载</h3>
<p>脚本加载可以构建 HashTree，然后把构建的 HashTree 转成 JMeter 可执行的测试计划，进而执行测试用例。HashTree 是 JMeter API 中不可缺少的一种数据结构，在 JMeter API 中，HashTree 有 2 种构建方式，分别是<strong>本地脚本加载</strong>和<strong>创建脚本文件</strong>。</p>
<p>先来说<strong>本地脚本加载</strong>的方式。用 JMeter 客户端手动生成 jmx 脚本文件后，我们可以通过 SaveService.loadTree 解析本地的 jmx 文件来运行脚本，核心步骤如下：</p>
<pre><code>//加载本地 jmx 脚本

HashTree jmxTree = SaveService.loadTree(file);
</code></pre>
<p>由于本地脚本是 JMeter 客户端手动生成的，所以这里只需要做读取文件操作即可，loadTree 会把 jmx 文件转成内存对象，并返回内存对象中生成的 HashTree。</p>
<p>那<strong>创建脚本文件</strong>是怎么做的呢？它是通过 API 构建测试计划，然后再保存为 JMeter 的 jmx 文件格式。核心步骤如下图所示：</p>
<p><img src="assets/Cip5yGAFPLWAE3XRAAHi31Yd_oY766.png" alt="Drawing 2.png" /></p>
<p>图 3：脚本文件创建步骤</p>
<p>该方式需要自己构建 HashTree，我们可以参考 JMeter 客户端生成的 jmx 文件。</p>
<p>通过观察 jmx 文件我们可以知道需要构建的 jmx 结构，最外层是 TestPlan，TestPlan 是 HashTree 结构，包含 ThreadGroup（线程组）、HTTPSamplerProxy、LoopController（可选）、ResultCollector（结果收集）等节点。</p>
<p>接下来我将讲解 JMeter API 创建脚本文件的 6 个步骤，这 6 个步骤也是我们通过 JMeter 客户端创建脚本最常用的步骤，它们依次是创建测试计划、创建 ThreadGroup、创建循环控制器、创建 Sampler、创建结果收集器以及构建 tree，生成 jmx 脚本。</p>
<p><strong>（1）创建测试计划</strong></p>
<p>先生成一个 testplan，之后所有的测试活动都在 testplan 下面进行。代码如下：</p>
<pre><code>try {

    TestPlan testPlan = new TestPlan(&quot;创建 JMeter 测试脚本&quot;);

    testPlan.setProperty(TestElement.TEST_CLASS, TestPlan.class.getName());

    testPlan.setProperty(TestElement.GUI_CLASS, TestPlanGui.class.getName());

    testPlan.setUserDefinedVariables((Arguments) new ArgumentsPanel().createTestElement());
</code></pre>
<p>通过以上代码，我们生成了 testplan。</p>
<p><strong>（2）创建 ThreadGroup</strong></p>
<p>ThreadGroup 是我们平时使用的线程组插件，它可以模拟并发用户数，一个线程通常认为是模拟一个用户。代码如下：</p>
<pre><code>    ThreadGroup threadGroup = new ThreadGroup();

    threadGroup.setName(&quot;Example Thread Group&quot;);

    threadGroup.setNumThreads(1);

    threadGroup.setRampUp(1);

    threadGroup.setSamplerController(loopController);

    threadGroup.setProperty(TestElement.TEST_CLASS, ThreadGroup.class.getName());

    threadGroup.setProperty(TestElement.GUI_CLASS, ThreadGroupGui.class.getName());
</code></pre>
<p>以上是我们使用 JMeter API 创建 ThreadGroup 的代码，它实现了我们线程数的设置，如启动设置等。</p>
<p><strong>（3）创建循环控制器</strong></p>
<p>这一步是一个可选项。我们在实际测试过程中，可以选择多线程的循环或者按时间段进行。创建循环控制器是为了模拟一个用户多次进行同样操作的行为，不创建循环控制器则默认是只执行一次操作。循环控制器创建的代码如下：</p>
<pre><code>    LoopController loopController = new LoopController();

    //设置循环次数，1 代表循环 1 次

    loopController.setLoops(1);

    loopController.setFirst(true);

    loopController.setProperty(TestElement.TEST_CLASS, LoopController.class.getName());

    loopController.setProperty(TestElement.GUI_CLASS, LoopControlPanel.class.getName());

    loopController.initialize()
</code></pre>
<p><strong>（4）创建 Sampler</strong></p>
<p>这一步来创建我们的实际请求，也是我们 JMeter 真正要执行的内容。以 HttpSampler 为例，创建 HttpSampler 是为了设置请求相关的一些信息，JMeter API 执行脚本的时候就可以根据我们设置的一些信息（比如请求地址、端口号、请求方式等）发送 HTTP 请求。</p>
<pre><code>    // 2.创建一个 HTTP Sampler - 打开 本地一个模拟地址

    HTTPSamplerProxy httpSamplerProxy = new HTTPSamplerProxy();

    httpSamplerProxy.setDomain(&quot;127.0.0.1:8080/index&quot;);

    httpSamplerProxy.setPort(80);

    httpSamplerProxy.setPath(&quot;/&quot;);

    httpSamplerProxy.setMethod(&quot;GET&quot;);

    httpSamplerProxy.setName(&quot;Open ip&quot;);

    httpSamplerProxy.setProperty(TestElement.TEST_CLASS, HTTPSamplerProxy.class.getName());

    httpSamplerProxy.setProperty(TestElement.GUI_CLASS, HttpTestSampleGui.class.getName());
</code></pre>
<p>以上按照一个 HTTP 的请求方式设置了 IP、端口等。</p>
<p><strong>（5）创建结果收集器</strong></p>
<p>结果收集器可以保存每次 Sampler 操作完成之后的结果的相关数据，例如，每次接口请求返回的状态、服务器响应的数据。</p>
<p>我们可以根据结果数据做一些性能指标计算返回给前端，如果在这里创建了结果收集器，那第 4 个阶段“结果收集”中就不用再创建了。创建代码如下：</p>
<pre><code>    ResultCollector resultCollector = new ResultCollector();

    resultCollector.setName(ResultCollector.class.getName());
</code></pre>
<p><strong>（6）构建 tree，生成 jmx 脚本</strong></p>
<p>以上第 2 步到第 5 步其实都是创建了一个 HashTree 的节点，就像我们用准备好的零件去拼装一辆赛车。我们把创建的这 4 个节点都添加到一个新建的子 HashTree 节点中，然后把子 HashTree 加到第 1 步的 testplan 中，最后再把 tesplan 节点加到构建好的父 HashTree 节点，这样就生成了我们的脚本可执行文件 jmx。代码如下：</p>
<pre><code>    HashTree subTree = new HashTree();

    subTree.add(httpSamplerProxy);

    subTree.add(loopController);

    subTree.add(threadGroup);

    subTree.add(resultCollector);

    HashTree tree = new HashTree();

    tree.add(testPlan,subTree);

    SaveService.saveTree(tree, new FileOutputStream(&quot;test.jmx&quot;));

} catch (IOException e) {

    e.printStackTrace();

}
</code></pre>
<p>通过以上代码我们可以创建出 JMeter 可识别的 HashTree 结构，并且可以通过 saveTree 保存为 test.jmx 文件。</p>
<p>到这里我们就完成了创建脚本文件的流程。我在这一讲的开始提到：<strong>脚本加载可以构建 HashTree</strong>，<strong>然后把构建的 HashTree 转成 JMeter 可执行的测试计划</strong>，<strong>进而执行测试用例</strong>。因此，我们接下来进入第 3 个阶段：测试执行。</p>
<h3>测试执行</h3>
<p>通过脚本文件的执行（测试执行），我们便可以开始对服务器发起请求，进行性能测试。测试执行主要包括 2 个步骤：</p>
<ol>
<li>把可执行的测试文件加载到 StandardJMeterEngine；</li>
<li>通过 StandardJMeterEngine 的 run 方法执行，便实现了 Runable 的接口，其中 engine.run 执行的便是线程的 run 方法。</li>
</ol>
<pre><code>//根据 HashTree 执行测试用例

StandardJMeterEngine engine = new StandardJMeterEngine();

engine.configure(jmxTree);

engine.run();
</code></pre>
<p>通过以上代码，我们完成了代码方式驱动 JMeter 执行的核心步骤。</p>
<h3>结果收集</h3>
<p>性能实时数据采集可以更方便发现和分析出现的性能问题。我们在性能测试平台的脚本页面点击执行了性能测试脚本，当然希望能看到实时压测的性能测试数据，如果等测试完再生成测试报告，时效性就低了。</p>
<p>性能测试平台结果收集的流程图如下：</p>
<p><img src="assets/CgpVE2AFPMiAUfRUAAHZ0vk2YZg058.png" alt="Drawing 3.png" /></p>
<p>图 4：结果收集流程图</p>
<p>上面流程图中与 JMeter 关联最密切的是第 1 步，获取 JMeter 结果数据。那我们如何获取这些数据呢？</p>
<p>JMeter 性能测试用例执行完成之后会生成结果报告，既然生成了结果报告，那 JMeter 源码里一定有获取每次 loop 执行结果的地方。我们可以找到这个类，然后新建一个类去继承这个类，再重写每次结果获取的方法就能得到实时结果了。如果获取每次 loop 执行结果的是私有方法，我们也可以通过反射拿到它。</p>
<p>既然是这样，那关键就是找到， JMeter 执行中是在哪个类、哪个方法里拿的每次 loop 的结果。</p>
<p>通过查看 JMeter API 可以发现，JMeter API 提供了一个结果收集器（ResultCollector），从结果收集器的源码中可以找到获取每次 loop 执行结果的方法。结果收集器的部分源码如下所示：</p>
<pre><code>/**

* When a test result is received, display it and save it.

*

* @param event

*            the sample event that was received

*/

@Override

public void sampleOccurred(SampleEvent event){...}
</code></pre>
<p>分析以上代码得知，我们可以重写 sampleOccurred 方法来收集每次 loop 的结果。该方法的参数 SampleEvent 中有我们需要的实时监控数据，这样实时监控就变得简单了。接下来，我以<strong>单客户端获取 QPS 实时监控数据</strong>为例，讲解性能测试平台结果收集相关代码实现的思路。</p>
<p>单客户端获取 QPS 实时监控数据，首先需要新建一个类继承 ResultCollector，并且重写 sampleOccurred 方法，但是这里有个问题：<strong>怎么接收 SampleEvent 里面的实时监控数据，或者说怎么取出来在我们的业务代码里应用呢</strong>？我们可以在 sampleOccurred 把监控数据存起来，然后写个接口读取存储的数据返回给前端。</p>
<p>图 4 中有一个中间件，这个中间件可以是<strong>内存数据库</strong>，也可以是<strong>消息组件</strong>，根据中间件的不同有以下 2 种实现方式。</p>
<ol>
<li><strong>把需要的监控数据存在静态 map 里</strong>，<strong>接口读取 map 里的数据返回给前端</strong>。这种方法虽然有利于初学者快速实现，但它的数据是存在内存中的 ，并且没有做持久化处理，容易出现丢失的情况，所以我们一般只在演示中使用。</li>
<li><strong>把数据存到消息队列里面</strong>，<strong>接口将消费队列的数据返回给前端</strong>。这是目前在互联网公司中较为常用的使用方式，在高并发下可靠性也不错。</li>
</ol>
<p>下面我来讲解下第 2 种方式的代码：</p>
<ul>
<li>新建一个类继承 ResultCollector 重写 sampleOccurred 方法，使用 Kafka 接收消息；</li>
</ul>
<pre><code>public class CCTestResultCollector extends ResultCollector {

    public static final String REQUEST_COUNT = &quot;requestCount&quot;;

    public CCTestResultCollector() {

        super();

    }

    public CCTestResultCollector(Summariser summer) {

        super(summer);

    }

    @Override

    public void sampleOccurred(SampleEvent event) {

        super.sampleOccurred(event);

        ......

        //代码片段,使用 kafka 发送消息

        producer.send(new ProducerRecord&lt;String,Integer&gt;(&quot;monitorData&quot;,&quot;requestCount&quot;, requestCountMap.get(REQUEST_COUNT) == null ? 0 : (requestCountMap.get(REQUEST_COUNT) + 1)));

    }

}
</code></pre>
<ul>
<li>后端获取存储的实时采集数据，这一步是后端获取数据并进行计算，生成的数据给前端展示使用。</li>
</ul>
<pre><code>@PostMapping(&quot;getMonitorData&quot;)

    public Result getMonitorData(@RequestBody MonitorDataReq monitorDataReq) {

        Map&lt;String,Object&gt; monitorDataMap = new HashMap&lt;&gt;();

        Long monitorXData = monitorDataReq.getMonitorXData();

        ......

   //kafka 消费消息代码片段，仅做示例演示

while (true) {

            //获取 ConsumerRecords，一秒钟轮训一次

            ConsumerRecords&lt;String, String&gt; records = consumer.poll(Duration.ofMillis(1000));

            //消费消息，遍历 records

            for (ConsumerRecord&lt;String, String&gt; r : records) {

                System.out.println(r.key() + &quot;:&quot; + r.value());

                if(&quot;requestCount&quot;.equals(r.key())){

                  //r.value 便可以获取到我们上个代码片段发送的消息，然后对 requestCount 做计算，计算后的值 put 到 monitorDataMap 后返回给前端；

                  ......

                }

            }

        }

        return Result.resultSuccess(null, monitorDataMap, ResultType.GET_PERFORMANCE_REPORT_SUCCE

        }
</code></pre>
<p>实现后的效果图如下：</p>
<p><img src="assets/Cip5yGAFPNWAIzKMAACkBrnfdmY418.png" alt="Drawing 4.png" /></p>
<p>图 5 ：效果图</p>
<blockquote>
<p>其中横坐标是时间，纵坐标是实时处理能力的展示，可以看到每秒请求次数在 400 ~ 600 之间波动。</p>
</blockquote>
<h3>总结</h3>
<p>这一讲我主要介绍了性能测试平台的功能模块划分，JMeter API 核心功能的 4 个阶段：环境初始化、脚本加载、测试执行和结果收集，并对脚本构建的 2 种方式和获取监控数据部分的代码实现思路做了一个详细的分析，同时贴出了关键部分的代码。</p>
<p>希望这一讲能够对你在开发性能测试平台时有所帮助，特别是关于平台实现还没有找到切入点的同学，性能测试平台开发相关的大多数需求都可以在这一讲的基础上扩展。</p>
<p>到此，我们对于工具的学习也告一段落了，通过<strong>模块一</strong>的学习，你不仅知道了工具的原理，还知道了它们的基础使用方法以及拓展方法。希望你也能在日常工作中，把这些工具用起来，有任何问题，都欢迎在留言区交流。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="04&#32;&#32;JMeter&#32;二次开发其实并不难.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="06&#32;&#32;Nginx&#32;在系统架构中的作用.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435b75893c645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
