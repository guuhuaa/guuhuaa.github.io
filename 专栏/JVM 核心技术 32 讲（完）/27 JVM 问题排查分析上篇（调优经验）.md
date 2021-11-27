<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>27 JVM 问题排查分析上篇（调优经验）.md</title>
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

                    
                    <a href="01&#32;阅读此专栏的正确姿势.md">01 阅读此专栏的正确姿势.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;环境准备：千里之行，始于足下.md">02 环境准备：千里之行，始于足下.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;常用性能指标：没有量化，就没有改进.md">03 常用性能指标：没有量化，就没有改进.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;JVM&#32;基础知识：不积跬步，无以至千里.md">04 JVM 基础知识：不积跬步，无以至千里.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;Java&#32;字节码技术：不积细流，无以成江河.md">05 Java 字节码技术：不积细流，无以成江河.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;Java&#32;类加载器：山不辞土，故能成其高.md">06 Java 类加载器：山不辞土，故能成其高.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;Java&#32;内存模型：海不辞水，故能成其深.md">07 Java 内存模型：海不辞水，故能成其深.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;JVM&#32;启动参数详解：博观而约取、厚积而薄发.md">08 JVM 启动参数详解：博观而约取、厚积而薄发.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;JDK&#32;内置命令行工具：工欲善其事，必先利其器.md">09 JDK 内置命令行工具：工欲善其事，必先利其器.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;JDK&#32;内置图形界面工具：海阔凭鱼跃，天高任鸟飞.md">10 JDK 内置图形界面工具：海阔凭鱼跃，天高任鸟飞.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;JDWP&#32;简介：十步杀一人，千里不留行.md">11 JDWP 简介：十步杀一人，千里不留行.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;JMX&#32;与相关工具：山高月小，水落石出.md">12 JMX 与相关工具：山高月小，水落石出.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;常见的&#32;GC&#32;算法（GC&#32;的背景与原理）.md">13 常见的 GC 算法（GC 的背景与原理）.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;常见的&#32;GC&#32;算法（ParallelCMSG1）.md">14 常见的 GC 算法（ParallelCMSG1）.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;Java11&#32;ZGC&#32;和&#32;Java12&#32;Shenandoah&#32;介绍：苟日新、日日新、又日新.md">15 Java11 ZGC 和 Java12 Shenandoah 介绍：苟日新、日日新、又日新.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;Oracle&#32;GraalVM&#32;介绍：会当凌绝顶、一览众山小.md">16 Oracle GraalVM 介绍：会当凌绝顶、一览众山小.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;GC&#32;日志解读与分析（基础配置）.md">17 GC 日志解读与分析（基础配置）.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;GC&#32;日志解读与分析（实例分析上篇）.md">18 GC 日志解读与分析（实例分析上篇）.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;GC&#32;日志解读与分析（实例分析中篇）.md">19 GC 日志解读与分析（实例分析中篇）.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;GC&#32;日志解读与分析（实例分析下篇）.md">20 GC 日志解读与分析（实例分析下篇）.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;GC&#32;日志解读与分析（番外篇可视化工具）.md">21 GC 日志解读与分析（番外篇可视化工具）.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;JVM&#32;的线程堆栈等数据分析：操千曲而后晓声、观千剑而后识器.md">22 JVM 的线程堆栈等数据分析：操千曲而后晓声、观千剑而后识器.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;内存分析与相关工具上篇（内存布局与分析工具）.md">23 内存分析与相关工具上篇（内存布局与分析工具）.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;内存分析与相关工具下篇（常见问题分析）.md">24 内存分析与相关工具下篇（常见问题分析）.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;FastThread&#32;相关的工具介绍：欲穷千里目，更上一层楼.md">25 FastThread 相关的工具介绍：欲穷千里目，更上一层楼.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;面临复杂问题时的几个高级工具：它山之石，可以攻玉.md">26 面临复杂问题时的几个高级工具：它山之石，可以攻玉.md</a>

                </li>
                <li>

                    <a class="current-tab" href="27&#32;JVM&#32;问题排查分析上篇（调优经验）.md">27 JVM 问题排查分析上篇（调优经验）.md</a>
                    

                </li>
                <li>

                    
                    <a href="28&#32;JVM&#32;问题排查分析下篇（案例实战）.md">28 JVM 问题排查分析下篇（案例实战）.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;GC&#32;疑难情况问题排查与分析（上篇）.md">29 GC 疑难情况问题排查与分析（上篇）.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;GC&#32;疑难情况问题排查与分析（下篇）.md">30 GC 疑难情况问题排查与分析（下篇）.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;JVM&#32;相关的常见面试问题汇总：运筹策帷帐之中，决胜于千里之外.md">31 JVM 相关的常见面试问题汇总：运筹策帷帐之中，决胜于千里之外.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;应对容器时代面临的挑战：长风破浪会有时、直挂云帆济沧海.md">32 应对容器时代面临的挑战：长风破浪会有时、直挂云帆济沧海.md</a>

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
                        <div><h1>27 JVM 问题排查分析上篇（调优经验）</h1>
<p>一般来说，只要系统架构设计得比较合理，大部分情况下系统都能正常运行，出现系统崩溃等故障问题是小概率事件。也就是说，业务开发是大部分软件工程中的重头戏，所以有人开玩笑说：“面试造火箭，入职拧螺丝。”</p>
<p>一般来说，我们进行排查分析的目的主要有：</p>
<ul>
<li>解决问题和故障</li>
<li>排查系统风险隐患</li>
</ul>
<p>我们按照问题的复杂程度，可以分为两类：</p>
<ul>
<li>常规问题</li>
<li>疑难杂症</li>
</ul>
<p>常规的问题一般在开发过程中就被发现和解决了，所以线上问题一般会比较复杂，出现在大家都没有考虑到的地方。按照我们的多年解决经验，这些复杂问题的排查方式可以分为两种途径：</p>
<ul>
<li>逻辑严密的系统性排查；</li>
<li>以猜测来驱动，凭历史经验进行排查。</li>
</ul>
<p>如果您倾向于选择后一种方式，那么可能会浪费大量的时间，效果得看运气。更糟糕的是，因为基本靠蒙，所以这个过程是完全不可预测的，如果时间很紧张，就会在团队内部造成压力，甚至升级为甩锅和互相指责。</p>
<p><img src="assets/7e9de660-79aa-11ea-9164-d34ec3ae1078" alt="66772038.png" /></p>
<p>系统出现性能问题或者故障，究竟是不是 JVM 的问题，得从各个层面依次进行排查。</p>
<h3>为什么问题排查这么困难？</h3>
<h4><strong>生产环境中进行故障排查的困难</strong></h4>
<p>在生产环境中针对特定问题进行故障排除时，往往会有诸多限制，从而导致排查的过程变得痛苦。</p>
<p><strong>1. 影响到客户的时间越短越好</strong></p>
<p>面对客户的抱怨，解决问题最快的办法可能是：“<strong>只要重启机器就能让系统恢复正常</strong>”。</p>
<p>用最快的方法来避免对用户产生影响是很自然的需求。</p>
<p>但重启可能会破坏故障现场，那样就很难排查问题的根本原因了。</p>
<p>如果重新启动实例，则无法再采集实际发生的情况，导致我们并没有从这次故障中学习，从而获得收益。</p>
<p>即使重启解决了目前的问题，但问题原因本身仍然存在，一直是一个定时炸弹，还可能会接二连三地发生。</p>
<p><strong>2. 安全方面的限制</strong></p>
<p>接下来是安全性相关的限制，这些限制导致生产环境是独立和隔离的，一般来说，开发人员可能没有权限访问生产环境。如果没有权限访问生产环境，那就只能进行远程故障排除，并涉及到所有与之相关的问题：</p>
<ul>
<li>每个要执行的操作都需要多人参与或审核，这不仅增加了执行单个操作所需的时间，而且沟通交流过程中可能会丢失一些信息。</li>
</ul>
<p>特别是将临时补丁程序发布到生产环境时，“希望它能生效”，但这种试错的情况却可能导致越来越糟糕。</p>
<p><strong>因为测试和发布流程可能又要消耗几小时甚至几天</strong>，进一步增加了解决问题实际消耗的时间。</p>
<p>如果还需要分多次上线这种“不一定生效的补丁程序”，则很可能会消耗几个星期才能解决问题。</p>
<p><strong>3. 工具引发的问题</strong></p>
<p>还有很重要的一点是需要使用的工具：<strong>安装使用的某些工具在特点场景下可能会使情况变得更糟</strong>。</p>
<p>例如：</p>
<ul>
<li>对 JVM 进行堆转储（heap dump）可能会使 JVM 暂停几十秒或更长时间。</li>
<li>打印更细粒度的日志可能会引入其他的并发问题，IO 开销、磁盘问题等。</li>
<li>增加的探测器或者分析器可能会有很大开销，导致本就缓慢的系统彻底卡死。</li>
</ul>
<p>因此，要想给系统打补丁或者增加新的远程监测程序，可能最终会花费很多天的时间：既然在生产环境中进行故障诊断排查会面临这么多的问题，很自然地，大部分情况下，我们都是在开发或测试环境中进行故障排查。</p>
<h4><strong>在测试和开发环境进行诊断需要注意的问题</strong></h4>
<p>如果在开发环境或者测试环境中进行问题诊断和故障排查，则可以避免生产环境中的那些麻烦。</p>
<p>因为开发环境和生产环境配置不同，有些时候可能也会有问题：即很难复现生产环境中产生的 Bug 或性能问题。</p>
<p>例如：</p>
<ul>
<li>测试环境和生产环境使用的数据源不同。这意味着由数据量引发的性能问题可能不会在测试环境中重现。</li>
<li>某些问题的使用方式可能不容易复现（我们有时候也称之为“幽灵问题”）。例如只在 2 月 29 日这个特殊时间引起的并发问题，只在多个用户同时访问某个功能时引发，如果事先不知道原因，那也很难排查。</li>
<li>两个环境下的应用程序可能还不一样。生产部署的配置可能明显不同。这些差异包括：操作系统、群集、启动参数，以及不同的打包版本。</li>
</ul>
<p>这些困难会引起“这不可能，我机器上就没事” 这种很尴尬的局面。</p>
<p>可以看出，因为和实际的生产环境不同，所以在对某些问题进行故障排除时，当前系统环境的性质可能会让你遇到的一些莫名其妙的障碍。</p>
<p>除了特定环境的约束之外，还有其他方面的因素也会导致故障排除过程的不可预测性。</p>
<h3>需要做哪些准备工作</h3>
<p>本节提供一些处理经验，但是我们希望他们不会成为你的应急措施（就像医生不希望你来医院）。</p>
<p>最好是在平时就先做好全面的系统监控、有针对性的应急预案，并时常进行演练。</p>
<h4><strong>掌握行业领域相关的知识</strong></h4>
<p>能力可以分为外功和内功。内功就是各种基础知识。外功就是各种工具、技能和技巧。</p>
<p>分析排查问题，需要大量的专业背景知识来支撑。否则你猜都不知道怎么猜，没有方向，也就很难验证正确性了。</p>
<p>想要具备排查复杂问题的能力，至少得对领域行业相关的横向知识有一定的了解，最好还能对所面临的具体问题域有竖向的深刻认识和经验，即所谓的“T”字型人才。</p>
<p>JVM 问题排查需要掌握哪些领域相关的知识呢？下面列出了一些基础：</p>
<ul>
<li>Java 语言功底</li>
<li>JVM 基础知识</li>
<li>并发领域知识</li>
<li>计算机体系结构和组成原理</li>
<li>TCP/IP 网络体系知识</li>
<li>HTTP 协议和 Nginx 等服务器知识</li>
<li>数据库领域知识</li>
<li>搜索引擎使用技巧</li>
</ul>
<p>以及从这些领域延伸出来的各种技能和技巧。</p>
<p>故障排除是必不可少的过程。只要有人使用的系统，就无法避免地会发生一些故障，因此我们需要很清楚地了解系统的现状和问题。我们无法绕过不同环境带来的困扰，但也不可能“21 天就变成专家”。</p>
<p>在技术开发这个行业，一万小时理论总是成立的。除了累积1万小时的训练时间来成为该领域的专家之外，其实还有更快速的解决方案来减轻故障排除所带来的痛苦。</p>
<h4><strong>在开发环境中进行抽样分析</strong></h4>
<p>对代码进行抽样分析并没有错，尤其是在系统正式上线之前。</p>
<p>相反，了解应用程序各个部分的热点以及内存消耗，能有效防止某些问题影响到生产环境的用户。</p>
<p>虽然由于数据，使用方式和环境的差异，最终只能模拟生产环境中面临的一部分问题。 但使用这种技术可以预先进行风险排查，如果真的发生问题，可以在追溯问题原因时很快定位。</p>
<h4><strong>在测试环境中进行验证</strong></h4>
<p>在质量保证领域投入适当的资源，尤其是自动化的持续集成、持续交付流程能及早暴露出很多问题。如果进行周全和彻底的测试，将进一步减少生产环境的事故。但是，这些工作往往得不到资源，“你看功能不是已经完成了吗，为什么还要去花人力物力继续搞，又没有收益”。</p>
<p>实际的工作中，我们很难证明对质量检查的投资是否合理。</p>
<p>一切标有“性能测试”或“验收测试”的产品，最终都将与清晰而可衡量的业务目标（新功能开发）存在竞争。</p>
<p>现在，当开发人员推动“执行某项性能优化”的任务时，如果不能提升优先级，此类任务会积压下来，永远都是待办事项。</p>
<p>为了证明这种投资的合理性，我们需要将投资回报与质量联系起来。如果将生产环境中的P1故障事件减少到80%，可以让我们多产生2倍的收益，在这种情况下，我们就能推动相关人员把这些工作做好。相反地，如果我们不能说明我们改进工作的收益，则我们可能就没有资源去提升质量。</p>
<blockquote>
<p>曾经有一个特别形象的例子：农村的孩子为什么不读书？</p>
<p>家长说：因为穷，所以不读书。</p>
<p>那又为什么而贫穷呢？</p>
<p>家长说：因为不读书，所以穷。</p>
</blockquote>
<h4><strong>在生产环境中做好监控</strong></h4>
<p>系统就像是人体一样，只要活着就会在某个时间点生病，所以，我们必须接受的第一件事情就是生产环境一定会出现问题，不管是 Bug 引起的，还是人为操作失误，亦或者天灾导致的。</p>
<p>即使是 NASA/SpaceX 这种高端组织也会不时地炸几艘飞船火箭，因此我们需要为线上发生的问题做好准备。</p>
<p>无论怎么分析和测试，总会有些漏掉的地方，事故就在这些地方产生。</p>
<p>既然无法避免总会需要对生产环境进行故障排除。为了更好地完成手头的工作，就需要监控生产环境中系统的状态。</p>
<ul>
<li>当出现问题时，理想情况下，我们已经拥有了足以解决该问题的相关信息。</li>
<li>如果已经拥有了所需的信息，则可以快速跳过问题复现和信息收集的步骤。</li>
</ul>
<p>不幸的是，监控领域并没有万能的银弹。即使是最新的技术也无法提供不同场景下的所有信息。</p>
<p>典型的 Web 应用系统，至少应该集成下面这些部分：</p>
<ul>
<li>日志监控。汇总各个服务器节点的日志，以便技术团队可以快速搜索相关的信息，日志可视化，并进行异常报警。最常用的解决方案是 ELK 技术栈，将日志保存到 <a href="https://www.elastic.co/">Elasticsearch</a> 中，通过 <a href="https://www.elastic.co/products/logstash">Logstash</a> 进行分析，并使用 <a href="https://www.elastic.co/products/kibana">Kibana</a> 来展示和查询。</li>
<li>系统监控。在基础架构中汇总系统指标并进行可视化查询，既简单又有效。关注CPU、内存、网络和磁盘的使用情况，可以发现系统问题并配置监控报警。</li>
<li>系统性能监控（APM，Application Performance Monitoring），以及用户体验监控。关注单个用户的交互，能有效展示用户感受到的系统性能和可用性问题。至少，我们可以知道是哪个服务在哪段时间发生了故障。比如集成 Micrometer、Pinpoint、Skywalking、Plumbr 等技术，能快速定位代码中的问题。</li>
</ul>
<p>确保在系统发布之前已经在开发环境中进行过系统性能分析，并经过测试验收，从而减少生产故障。</p>
<p>了解生产部署环境并做好监控，当故障发生时，我们就能可预料的方式，更快地做出响应。</p>
<h3>自上而下划分 JVM 问题</h3>
<p>前面的小节讲了一般的问题诊断和调优套路：</p>
<blockquote>
<p>做好监控，定位问题，验证结果，总结归纳。</p>
</blockquote>
<p>下面我们看看 JVM 领域有哪些问题.</p>
<p><img src="assets/485cc7f0-79ab-11ea-9057-3b1d25666613" alt="47867364.png" /></p>
<p>从上图可以看到，JVM 可以划分为这些部分：</p>
<ul>
<li>执行引擎，包括：GC、JIT 编译器</li>
<li>类加载子系统，这部分的问题，一般在开发过程中出现</li>
<li>JNI 部分，这部分问题一般在 JVM 之外</li>
<li>运行时数据区；Java 将内存分为 2 大块：堆内存和栈内存</li>
</ul>
<p>对这些有了了解，在我们进行知识储备时，就可以按照自顶向下的方式，逐个攻克。</p>
<p>线上环境的JVM问题主要集中在 GC 和内存部分。而栈内存、线程分析等问题，主要是辅助诊断 Java 程序本身的问题。</p>
<p>相关的知识点，如果有不清楚的地方，请各位同学回过头来，再读一读前面的章节。</p>
<p>我认为这些基础的技术和知识，需要阅读和练习 2~3 遍，才会掌握的比较牢固；毕竟理解和掌握了才是自己的。</p>
<h3>标准 JVM 参数配置</h3>
<p>有读者朋友提问：</p>
<blockquote>
<p>我希望能在课程中总结一下，JVM 的参数设置，应该按照哪些步骤来设置？</p>
</blockquote>
<p>截止目前（2020 年 3 月），JVM 可配置参数已经达到 1000 多个，其中 GC 和内存配置相关的 JVM 参数就有 600 多个。从这个参数比例也可以看出，JVM 问题排查和性能调优的重点领域还是 GC 和内存。</p>
<p>参数太多是个大麻烦，让人难以下手，学习和理解起来也很费事。</p>
<p>但在绝大部分业务场景下，常用的 JVM 配置参数也就 10 来个。</p>
<p>我们先给一个示例，读者可根据需要适当增减。</p>
<pre><code class="language-shell"># 设置堆内存
-Xmx4g -Xms4g 
# 指定 GC 算法
-XX:+UseG1GC -XX:MaxGCPauseMillis=50 
# 指定 GC 并行线程数
-XX:ParallelGCThreads=4 
# 打印 GC 日志
-XX:+PrintGCDetails -XX:+PrintGCDateStamps 
# 指定 GC 日志文件
-Xloggc:gc.log 
# 指定 Meta 区的最大值
-XX:MaxMetaspaceSize=2g 
# 设置单个线程栈的大小
-Xss1m 
# 指定堆内存溢出时自动进行 Dump
-XX:+HeapDumpOnOutOfMemoryError 
-XX:HeapDumpPath=/usr/local/

</code></pre>
<p>这些参数我们在前面的章节中都介绍过。</p>
<p>此外，还有一些常用的属性配置：</p>
<pre><code># 指定默认的连接超时时间
-Dsun.net.client.defaultConnectTimeout=2000
-Dsun.net.client.defaultReadTimeout=2000
# 指定时区
-Duser.timezone=GMT+08 
# 设置默认的文件编码为 UTF-8
-Dfile.encoding=UTF-8 
# 指定随机数熵源（Entropy Source）
-Djava.security.egd=file:/dev/./urandom 

</code></pre>
<h3>一份简单的问题排查手册</h3>
<h4><strong>一般人的排查方式</strong></h4>
<p>如果使用自己熟悉的工具，并且对于故障排除的规则已经胸有成竹，那么环境限制就不再是什么大问题。</p>
<p>实际上，负责排查和解决问题的工程师通常没有预先规划好的处理流程。</p>
<p>老实说，大家是否有过像下面这样的 shell 操作：</p>
<pre><code># 查看当前路径
pwd

# 查看当前目录下有哪些文件
ls -l

# 查看系统负载
top

# 查看剩余内存
free -h

# 查看剩余磁盘
df -h

# 查看当前目录的使用量
du -sh *

# 系统活动情况报告
sar
-bash: sar: command not found

# Linux安装sysstat
# apt-get install sysstat
# yum -y install sysstat

# 查看帮助手册
man sar

# 查看最近的报告
sar 1

# ???
sar -G 1 3
sar: illegal option -- G

# 查看帮助手册
man sar

# ......

</code></pre>
<p>如果您觉得上面这个过程很熟悉，别紧张，其实大家都这样干。</p>
<p>大多数工程师在故障排除和诊断调优领域都缺乏经验，因此也就很难使用标准的套路。</p>
<p>这没什么丢人的——除非是 <a href="http://www.brendangregg.com/">Brendan Gregg</a> or <a href="https://twitter.com/PeterLawrey">Peter Lawrey</a> 这种专业大牛，否则您很难有 1 万小时的故障排除经历，也就很难成为这个领域的专家。</p>
<p>缺乏经验的话，针对当前问题，往往需要使用不同的工具来收集信息，例如：</p>
<ul>
<li>收集不同的指标（CPU、内存、磁盘 IO、网络等等）</li>
<li>分析应用日志</li>
<li>分析 GC 日志</li>
<li>获取线程转储并分析</li>
<li>获取堆转储来进行分析</li>
</ul>
<p>最容易排查的是系统硬件和操作系统问题，比如：CPU、内存、网络、磁盘 IO。</p>
<p>我们可以使用的工具几乎是无限的。与实际解决问题相比，使用各种不熟悉的工具，可能会浪费更多的时间。</p>
<h4><strong>以可量化的方式来进行性能调优</strong></h4>
<p>回顾一下，我们的课程介绍了可量化的 3 个性能指标：</p>
<ul>
<li>系统容量：比如硬件配置、设计容量；</li>
<li>吞吐量：最直观的指标是 TPS；</li>
<li>响应时间：也就是系统延迟，包括服务端延时和网络延迟。</li>
</ul>
<p>也可以具体拓展到单机并发，总体并发、数据量；用户数、预算成本等等。</p>
<h4><strong>一个简单的流程</strong></h4>
<p>不同的场景、不同的问题，排查方式都不一样，具体怎么来确定问题是没有固定套路的。</p>
<p>可以事先进行的操作包括：</p>
<ul>
<li>培训：提前储备相关领域的知识点和技能、工具使用技巧等等。</li>
<li>监控：前面提到过，主要是 3 部分，业务日志、系统性能、APM 指标。</li>
<li>预警：在故障发生时，及时进行告警； 在指标超过阈值时进行预警。</li>
<li>排查风险点：了解系统架构和部署结构，分析单点故障、扩容瓶颈等等。</li>
<li>评估系统性能和服务级别：例如可用性、稳定性、并发能力、扩展性等等。</li>
</ul>
<p>各家公司可能有自己的事故处理规范，可能会涉及这些因素：</p>
<ul>
<li>相关人员：包括开发、运维、运营、QA、管理人员、客服等等。</li>
<li>事故级别，严重程度，影响范围、紧急程度。</li>
<li>汇报、沟通、咨询。</li>
<li>问题排查，诊断、定位，监控、分析</li>
<li>事故总结、分析原因、防止再现。</li>
<li>改进和优化、例如使用新技术、优化架构等等。</li>
</ul>
<h4><strong>可以进行排查的点</strong></h4>
<p>\1. 查询业务日志，可以发现这类问题：请求压力大、波峰、遭遇降级、熔断等等，基础服务、外部 API 依赖。</p>
<p>\2. 查看系统资源和监控信息：</p>
<ul>
<li>硬件信息、操作系统平台、系统架构</li>
<li>排查 CPU 负载</li>
<li>内存不足</li>
<li>磁盘使用量、硬件故障、磁盘分区用满、IO 等待、IO 密集、丢数据、并发竞争等情况</li>
<li>排查网络：流量打满，响应超时，无响应，DNS 问题，网络抖动，防火墙问题，物理故障，网络参数调整、超时、连接数</li>
</ul>
<p>\3. 查看性能指标，包括实时监控、历史数据。可以发现假死、卡顿、响应变慢等现象。</p>
<ul>
<li>排查数据库，并发连接数、慢查询、索引、磁盘空间使用量、内存使用量、网络带宽、死锁、TPS、查询数据量、redo 日志、undo、binlog 日志、代理、工具 Bug。可以考虑的优化包括：集群、主备、只读实例、分片、分区。</li>
<li>大数据、中间件、JVM 参数。</li>
</ul>
<p>\4. 排查系统日志，比如重启、崩溃、Kill。</p>
<p>\5. APM，比如发现有些链路请求变慢等等。</p>
<p>\6. 排查应用系统：</p>
<ul>
<li>排查配置文件：启动参数配置、Spring 配置、JVM 监控参数、数据库参数、Log 参数、APM 配置。</li>
<li>内存问题，比如是否存在内存泄漏，内存溢出、批处理导致的内存放大、GC 问题等等。</li>
<li>GC 问题，确定 GC 算法、确定 GC 的KPI，GC 总耗时、GC 最大暂停时间、分析 GC 日志和监控指标：内存分配速度，分代提升速度，内存使用率等数据。适当时修改内存配置。</li>
<li>排查线程，理解线程状态、并发线程数、线程 Dump，锁资源、锁等待、死锁。</li>
<li>排查代码，比如安全漏洞、低效代码、算法优化、存储优化、架构调整、重构、解决业务代码 Bug、第三方库、XSS、CORS、正则。</li>
<li>单元测试：覆盖率、边界值、Mock 测试、集成测试。</li>
</ul>
<p>\7. 排除资源竞争、[坏邻居效应](https://github.com/cncounter/translation/blob/master/tiemao_2016/45_noisy_neighbors/noisy_neighbor_cloud _performance.md)。</p>
<p>\8. 疑难问题排查分析手段：</p>
<ul>
<li>DUMP 线程</li>
<li>DUMP 内存</li>
<li>抽样分析</li>
<li>调整代码、异步化、削峰填谷</li>
</ul>
<p>总之，时至今日，软件领域的快速发展，使得我们可以使用的手段和工具，都很丰富。勤学苦练，掌握一些常见的套路，熟练搭配应用一些工具，是我们技术成长，能快速解决问题的不二法门。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="26&#32;面临复杂问题时的几个高级工具：它山之石，可以攻玉.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="28&#32;JVM&#32;问题排查分析下篇（案例实战）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4341253c9570ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/JVM%20%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%2032%20%E8%AE%B2%EF%BC%88%E5%AE%8C%EF%BC%89/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
