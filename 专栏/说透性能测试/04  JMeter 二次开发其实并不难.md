<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>04  JMeter 二次开发其实并不难.md</title>
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

                    <a class="current-tab" href="04&#32;&#32;JMeter&#32;二次开发其实并不难.md">04  JMeter 二次开发其实并不难.md</a>
                    

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
                        <div><h1>04  JMeter 二次开发其实并不难</h1>
<p>上一讲我们通过学习 JMeter 的脚本编写方式和执行方式，掌握了如何让 JMeter 更加有效地运行，其技术思路是使用 JMeter 本身或者社区提供的现成方案去实现，这基本已经满足了绝大多数性能测试的需求。</p>
<p>随着互联网行业发展，各种技术方案层出不穷，但是任何方案都不是万能的，有些需求是要我们自己写代码去实现的，JMeter 也留了相应的入口便于我们编写代码，所以本讲将介绍三种插件编写方式：</p>
<ul>
<li>自定义 BeanShell 功能</li>
<li>自定义请求编写（Java Sampler）</li>
<li>自定义函数助手</li>
</ul>
<h3>自定义 BeanShell 功能</h3>
<h4>什么是 BeanShell</h4>
<p>BeanShell 是由 Java 编写的，相当于一个小巧的 Java <strong>源码解释器</strong>，简单来说就是你可以在里面写代码，然后通过 Beanshell 翻译成插件可以识别的指令去执行相关操作。</p>
<h4>JMeter 中用 BeanShell 的优势</h4>
<p>JMeter 也是由 Java 编写的，而 Java 运行前需要先编译，而 BeanShell 作为一款解释器直接运行源代码就可以。</p>
<h4>BeanShell 在 JMeter 的作用</h4>
<p>BeanShell 在 JMeter 中有着广泛的应用，包括前置处理器、后置处理器、Sampler 等，我们来看下这些主要应用是做什么的。</p>
<ul>
<li>前置处理器：主要是在接口请求前做一些逻辑，生成参数化数据。</li>
<li>后置处理器：用于提取参数、参数格式设置等。</li>
<li>Sampler：可以作为独立的请求，支持各类请求编写、数据生成。</li>
</ul>
<h4>BeanShell 的常见用法举例</h4>
<p>对我来说，BeanShell 最常被用于对请求或者返回内容进行获取或者加工，其中 prev 是对当前的取样进行访问，执行了对响应状态码、响应信息、请求头等的操作，示例如下：</p>
<pre><code>log.info(&quot;code is  &quot;+prev.getResponseCode());

#获取响应的状态码

log.info(&quot;response is &quot;+prev.getResponseDataAsString());

#获取响应信息

log.info(&quot;content_type  &quot;+prev.getContentType());

#获取头文件中ContentType类型

log.info(&quot;header &quot;+prev.getRequestHeaders());

#获取取样器请求首部字段
</code></pre>
<p>通过以上方式，基本实现了对请求的基本信息的获取，然后你就可以对这些信息做进一步的提取、判断等操作。可能你会问我，使用 info 级别的日志打印，JMeter 还支持 error 级别的日志打印吗？答案是支持的，示例如下：</p>
<pre><code>log.error(&quot;cctester&quot;);

log.info(&quot;cctester&quot;);
</code></pre>
<p>你可以在 BeanShell 中自行验证下，使用 log 和 error 的方式对于 JMeter 的界面提示信息是否有区别。</p>
<p>JMeter 调用 BeanShell 解释器来运行脚本，同样需要注意的是不建议过度使用这个插件， 因为在 JMeter 高并发时，它将会<strong>消耗较多的本地资源</strong>，所以一般遇到逻辑相对复杂且代码量较大的情况，我们会使用 JMeter 的另一种特色功能：开发自定义插件（jar 形式），一般来说自定义的插件会帮助我们实现两方面功能：</p>
<ul>
<li>JMeter 本身需要自行拓展的请求或者不支持的测试协议，我们可以使用 Java 请求来完成；</li>
<li><strong>自定义辅助函数</strong>，协助我们进行性能测试。</li>
</ul>
<h3>自定义请求编写（Java Sampler）</h3>
<p>为了让你能够系统地学习 Java Sampler 的编写，我将分为如下四部分来介绍。</p>
<ul>
<li>什么是 Maven</li>
<li>什么是 Pom</li>
<li>实现 Java Sampler 功能的两种方式</li>
<li>实例：使用 Java Sampler 重写 POST 请求</li>
</ul>
<h4>什么是 Maven</h4>
<p>Maven 是一个<strong>项目管理工具</strong>，它可以很方便地管理项目依赖的第三方类库及其版本，说得再通俗一点：</p>
<ul>
<li>没有它之前你得手动下载对应的 jar，并且复制到项目里面，升级的话又得重新下载；</li>
<li>有了 Maven 之后你只需要填写依赖的包名词及其版本号，就能自动帮你下载对应的版本然后自动进行构建，如果说 Maven 只是名字或者代号，那么灵魂就是 Pom 了。</li>
</ul>
<h4>什么是 Pom</h4>
<p>在 Maven 里，project 可以没有代码，但是必须包含 pom.xml 文件。pom 文件是 Maven 对应的配置文件，我们依赖的相关信息可以在 pom.xml 中进行配置，它必须包含 modelVersion、groupId、artifactId 和 version 这四个元素，下面来看下这些元素具体的作用。</p>
<ul>
<li><strong>modelVersion</strong>：指定了当前 POM 模型的版本，对于 Maven 2 及 Maven 3 来说都是 4.0.0。</li>
</ul>
<pre><code>&lt;modelVersion&gt;4.0.0&lt;/modelVersion&gt;
</code></pre>
<ul>
<li><strong>groupId</strong>：组织标识、项目名称。</li>
</ul>
<pre><code>&lt;groupId&gt;com.cctester&lt;/groupId&gt;
</code></pre>
<ul>
<li><strong>artifactId</strong>：模块名称，当前项目组中唯一的 ID。</li>
</ul>
<pre><code>&lt;artifactId&gt;mavenTest&lt;/artifactId&gt;
</code></pre>
<ul>
<li><strong>version</strong>：项目当前的版本号。</li>
</ul>
<pre><code>&lt;version&gt;1.0-SNAPSHOT&lt;/version&gt;
</code></pre>
<ul>
<li><strong>packaging</strong>：打包格式，可以为 jar、war 等。</li>
</ul>
<pre><code>&lt;packaging&gt;jar&lt;packaging&gt;
</code></pre>
<p>开发之前在 pom 文件里引入相应的 jar 包，这些 jar 包会给我们提供相应的类或者接口，引入方式如下所示：</p>
<pre><code>&lt;dependency&gt;

    &lt;groupId&gt;org.apache.jmeter&lt;/groupId&gt;

    &lt;artifactId&gt;ApacheJMeter_core&lt;/artifactId&gt;

    &lt;version&gt;5.3&lt;/version&gt;

&lt;/dependency&gt;

&lt;dependency&gt;

    &lt;groupId&gt;org.apache.jmeter&lt;/groupId&gt;

    &lt;artifactId&gt;ApacheJMeter_java&lt;/artifactId&gt;

    &lt;version&gt;5.3&lt;/version&gt;

&lt;/dependency&gt;
</code></pre>
<h4><strong>实现 Java Sampler 功能的两种方式</strong></h4>
<ul>
<li>继承 AbstractJavaSamplerClient 抽象类；</li>
<li>实现 JavaSamplerClient 接口。</li>
</ul>
<p>通过阅读源码可以发现 AbstractJavaSamplerClient 抽象类是 JavaSamplerClient 接口的子类，想必我们都知道实现一个接口就必须实现接口里的所有方法，然而当你不需要实现所有方法时，继承 AbstractJavaSamplerClient 抽象类也是一个不错的选择。为了学习的全面性我就以实现 JavaSamplerClient 接口的方式去讲解所涉及的四个方法。</p>
<p>（1）如下所示，这个方法由 JMeter 在进行添加 JavaRequest 时第一个运行，它决定了你要在 GUI 中默认显示哪些属性。当每次在 GUI 里点击建立 java requst sampler 的时候会调用该方法。该方法设置了 parameters 的初始值，也可以在 sampler 的 GUI 界面做进一步的修改。</p>
<pre><code> public Arguments getDefaultParameters() {}
</code></pre>
<p>（2）如下所示，这个方法用于初始化测试脚本里面用到的变量，这些变量会在后续执行中使用。</p>
<pre><code> public void setupTest(JavaSamplerContext context) {}
</code></pre>
<p>（3）如下所示，<strong>这个方法是实现功能逻辑的主方法</strong>，每个线程会循环执行这个方法。</p>
<pre><code>public SampleResult runTest(JavaSamplerContext context) {}
</code></pre>
<ul>
<li>计时开始的时刻是从 SampleResult 类里面的 sampleStart() 方法执行开始。</li>
<li>计时结束的时刻是 sampleEnd() 方法执行结束。</li>
<li>setSuccessful() 方法用来表示测试的成功与否，通常使用 try catch 来设置结果，也可以用 if 语句。</li>
<li>setResponseData() 方法用来为测试结果传递数据。</li>
</ul>
<p>（4）如下所示，这个方法在每个线程执行完所有的测试工作之后执行，有点像 finally 的功能，比如，我开了一个数据库的连接，那么我要在所有的线程完成工作后关闭。</p>
<pre><code>public void teardownTest(JavaSamplerContext context) {}
</code></pre>
<h4>案例：使用 JavaSampler 重写 HTTP 的 POST 请求</h4>
<p>相信你在平时工作中会经常接触到 POST 请求，接下来我将举一个有更多代入感的例子。</p>
<p>（1）首先我们来完成 POST 请求的核心方法，先使用 HttpClients 发送构建的 POST 数据包，然后获取到返回值，这一步是完成 POST 请求的基本步骤，示例代码如下：</p>
<pre><code>//HttpClients提供功支持 HTTP 协议的客户端工具

httpClient = HttpClients.createDefault();

//新建一个HttpPost请求的对象将url，接口参数等信息传给这个对象

HttpPost httpPost = new HttpPost(URL);

//传入请求参数

httpPost.setEntity(new UrlEncodedFormEntity(Value, UTF8_CHARSET));

// 设置header信息，指定报文头Content-type等

httpPost.setHeader(&quot;Content-type&quot;, &quot;xxxxx&quot;)；

// 执行请求操作，并拿到结果

response = httpClient.execute(httpPost);
</code></pre>
<p>（2）接下来实现 JavaSamplerClient 接口，这是编写 Java Sampler 插件需要实现的核心接口，涉及的方法是 getDefaultParameters() 和 runTest()，作用上文已经描述过。下面带你来看具体怎么使用的，如下代码所示：</p>
<pre><code>//这是决定我们JMeter界面需要输入的内容，你可以看到有了url，username 和password信息，并且给出了默认值

public Arguments getDefaultParameters() {

    Arguments arguments = new Arguments();

    arguments.addArgument(&quot;url&quot;,&quot;127.0.0.1:9081&quot;);

    arguments.addArgument(&quot;username&quot;, &quot;cctester&quot;);

    arguments.addArgument(&quot;password&quot;, &quot;password&quot;);

    return arguments;

}
</code></pre>
<p>这一步实际的效果图可以看下方的初始界面图。</p>
<p><img src="assets/Cip5yGAFPAKAEmBcAAB8OFXAQYo399.png" alt="Drawing 0.png" /></p>
<p>初始界面图</p>
<p>（3）在上一步骤进行了参数的输入，接下来实现接收这些参数，并进行参数的输入、发送、返回判断等，如下代码所示：</p>
<pre><code>public SampleResult runTest(JavaSamplerContext javaSamplerContext) {

    //生成sampleResult对象，用于请求的命名、标记状态、添加返回内容等

    SampleResult sampleResult=new SampleResult();

    sampleResult.setSampleLabel(&quot;cctester_login&quot;);

    //调用上文中实现的post请求

    PostTest postTest=new PostTest();

    //接受JMeter界面上传输的参数

    String username = javaSamplerContext.getParameter(&quot;username&quot;);

    String password = javaSamplerContext.getParameter(&quot;password&quot;);

    String url = javaSamplerContext.getParameter(&quot;url&quot;);

    //标记请求开始

    sampleResult.sampleStart();

    try {

        HttpResponse result =postTest.Request(url,username,password);

        String entity= EntityUtils.toString(result.getEntity());

        //根据返回内容判断结果状态并展示结果

        if (result.getStatusLine().getStatusCode()==200){

            sampleResult.setSuccessful(true);

            sampleResult.setResponseCodeOK();

            sampleResult.setResponseData(entity, &quot;utf-8&quot;);

        }else {

            sampleResult.setSuccessful(false);

            sampleResult.setResponseData(entity, &quot;utf-8&quot;);

   ）
</code></pre>
<p>（4）完成后打成 jar 包放到 /lib/ext 下重启 JMeter 即可，实际的效果图你可以参考上方的初始界面图和下方的运行图。</p>
<p><img src="assets/Cip5yGAFPBOAecdTAAC22dYxB2Q653.png" alt="Drawing 1.png" /></p>
<p>运行图</p>
<h3>自定义函数助手</h3>
<p>通过 Java Sampler 插件开发的学习，我们知道 JMeter 相关插件的开发其实都是有一定的套路可循，那 JMeter 函数助手开发也不例外，接下来进行函数助手开发流程的了解。</p>
<p>（1）引入 Maven 包，这个包会给我们提供函数助手开发相关的类，如下代码所示：</p>
<pre><code>&lt;dependency&gt;

    &lt;groupId&gt;org.apache.jmeter&lt;/groupId&gt;

    &lt;artifactId&gt;ApacheJMeter_functions&lt;/artifactId&gt;

    &lt;version&gt;5.3&lt;/version&gt;

&lt;/dependency&gt;
</code></pre>
<p>（2）接下来新建我们的类包，此时新建的包需要特别注意，<strong>名字只能是 functions 结尾</strong>，否则打包放到 JMeter 中是没有办法识别这个插件的，然后代码中继承 AbstractFunction 类就可以实现，一起看下需要实现哪些方法。</p>
<pre><code>   public String getReferenceKey() {}
</code></pre>
<p>这一方法表示函数助手对话框中的下拉框中显示的函数名称，如下图所示：</p>
<p><img src="assets/Cip5yGAFPB6ADKzZAAB86ItSH7Q951.png" alt="Drawing 2.png" /></p>
<pre><code>public List&lt;String&gt; getArgumentDesc() {}
</code></pre>
<p>这一方法是设置入参的描述语，用于函数助手对话框中，显示函数名称提示。</p>
<pre><code>public void setParameters(Collection&lt;CompoundVariable&gt; collection) {}
</code></pre>
<p>这一方法用于我们的参数值传入。</p>
<pre><code>public String execute(SampleResult sampleResult, Sampler sampler){}
</code></pre>
<p>这一方法是根据入参，执行核心逻辑，保存结果至相应的变量中。</p>
<h3>总结</h3>
<p>通过本讲的学习，你知道了如何使用代码方式实现自己需要的插件，beanshell 和 jar 包引入都是工作中常见的，相信这部分知识会对你的工作产生比较大的帮助，这也是 JMeter 的特色功能，不仅落地性强而且社区资料完善。</p>
<p><strong>这里给你留个小作业</strong>：相信经过上文的讲解以及实例，你比较清楚地知道了插件开发的核心流程，你可以根据自己工作中的自定义函数助手的需求，按照上面的代码结构自行完成。在实践过程中遇到任何问题，欢迎在留言区留言。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="03&#32;&#32;构建并执行&#32;JMeter&#32;脚本的正确姿势.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="05&#32;&#32;如何基于&#32;JMeter&#32;API&#32;开发性能测试平台？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435b710c6f645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
