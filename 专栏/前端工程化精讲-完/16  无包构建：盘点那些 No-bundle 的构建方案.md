<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>16  无包构建：盘点那些 No-bundle 的构建方案.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;建立上帝视角，全面系统掌握前端效率工程化.md">00 开篇词  建立上帝视角，全面系统掌握前端效率工程化.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;项目基石：前端脚手架工具探秘.md">01  项目基石：前端脚手架工具探秘.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;界面调试：热更新技术如何开着飞机修引擎？.md">02  界面调试：热更新技术如何开着飞机修引擎？.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;构建提速：如何正确使用&#32;SourceMap？.md">03  构建提速：如何正确使用 SourceMap？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;接口调试：Mock&#32;工具如何快速进行接口调试？.md">04  接口调试：Mock 工具如何快速进行接口调试？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;编码效率：如何提高编写代码的效率？.md">05  编码效率：如何提高编写代码的效率？.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;团队工具：如何利用云开发提升团队开发效率？.md">06  团队工具：如何利用云开发提升团队开发效率？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;低代码工具：如何用更少的代码实现更灵活的需求.md">07  低代码工具：如何用更少的代码实现更灵活的需求.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;无代码工具：如何做到不写代码就能高效交付？.md">08  无代码工具：如何做到不写代码就能高效交付？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;构建总览：前端构建工具的演进.md">09  构建总览：前端构建工具的演进.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;流程分解：Webpack&#32;的完整构建流程.md">10  流程分解：Webpack 的完整构建流程.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;编译提效：如何为&#32;Webpack&#32;编译阶段提速？.md">11  编译提效：如何为 Webpack 编译阶段提速？.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;打包提效：如何为&#32;Webpack&#32;打包阶段提速？.md">12  打包提效：如何为 Webpack 打包阶段提速？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;缓存优化：那些基于缓存的优化方案.md">13  缓存优化：那些基于缓存的优化方案.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;增量构建：Webpack&#32;中的增量构建.md">14  增量构建：Webpack 中的增量构建.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;版本特性：Webpack&#32;5&#32;中的优化细节.md">15  版本特性：Webpack 5 中的优化细节.md</a>

                </li>
                <li>

                    <a class="current-tab" href="16&#32;&#32;无包构建：盘点那些&#32;No-bundle&#32;的构建方案.md">16  无包构建：盘点那些 No-bundle 的构建方案.md</a>
                    

                </li>
                <li>

                    
                    <a href="17&#32;&#32;部署初探：为什么一般不在开发环境下部署代码？.md">17  部署初探：为什么一般不在开发环境下部署代码？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;工具盘点：掌握那些流行的代码部署工具.md">18  工具盘点：掌握那些流行的代码部署工具.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;安装提效：部署流程中的依赖安装效率优化.md">19  安装提效：部署流程中的依赖安装效率优化.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;流程优化：部署流程中的构建流程策略优化.md">20  流程优化：部署流程中的构建流程策略优化.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;容器方案：从构建到部署，容器化方案的优势有哪些？.md">21  容器方案：从构建到部署，容器化方案的优势有哪些？.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;案例分析：搭建基本的前端高效部署系统.md">22  案例分析：搭建基本的前端高效部署系统.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;结束语&#32;&#32;前端效率工程化的未来展望.md">23 结束语  前端效率工程化的未来展望.md</a>

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
                        <div><h1>16  无包构建：盘点那些 No-bundle 的构建方案</h1>
<p>上节课我们讨论了 Webpack 的最新版本 Webpack 5 所带来的提效新功能。思考题是 Webpack 5 中的持久化缓存究竟会影响哪些构建环节呢？</p>
<p>通过对 compiler.cache.hook.get 的追踪不难发现：持久化缓存一共影响下面这些环节与内置的插件：</p>
<ul>
<li>编译模块：ResolverCachePlugin、Compilation/modules。</li>
<li>优化模块：FlagDependencyExportsPlugin、ModuleConcatenationPlugin。</li>
<li>生成代码：Compilation/codeGeneration、Compilation/assets。</li>
<li>优化产物：TerserWebpackPlugin、RealContentHashPlugin。</li>
</ul>
<p>正是通过这样多环节的缓存读写控制，才打造出 Webpack 5 高效的持久化缓存功能。</p>
<p>在之前的课程里我们详细分解了 Webpack 构建工具的效率优化方案，这节课我们来聊一聊今年比较火的另一种构建工具思路：无包构建（No-Bundle/Unbundle）。</p>
<h3>什么是无包构建</h3>
<p>什么是无包构建呢？这是一个与基于模块化打包的构建方案相对的概念。</p>
<p>在“ 第 9 课时|构建总览：前端构建工具的演进”中谈到过，目前主流的构建工具，例如 Webpack、Rollup 等都是基于一个或多个入口点模块，通过依赖分析将有依赖关系的模块<strong>打包到一起</strong>，最后形成少数几个产物代码包，因此这些工具也被称为<strong>打包工具</strong>。只不过，这些工具的构建过程除了打包外，还包括了模块编译和代码优化等，因此称为打包式构建工具或许更恰当。</p>
<p>而<strong>无包构建</strong>是指这样一类构建方式：在构建时只需处理模块的编译而<strong>无须打包</strong>，把模块间的**依赖关系完全交给浏览器来处理。**浏览器会加载入口模块，分析依赖后，再通过网络请求加载被依赖的模块。通过这样的方式简化构建时的处理过程，提升构建效率。</p>
<p>这种通过浏览器原生的模块进行解析的方式又称为 Native-ESM（Native ES Module）。下面我们就通过一个简单示例来展示这种基于浏览器的模块加载过程（<a href="https://github.com/fe-efficiency/lessons_fe_efficiency/tree/master/16_nobundle">16_nobundle</a>/simple-esm），如下面的代码和图片所示：</p>
<pre><code>//./src/index.html

...

&lt;script type=&quot;module&quot; src=&quot;./modules/foo.js&quot;&gt;&lt;/script&gt;

...

//.src/modules/foo.js

import { bar } from './bar.js'

import { appendHTML } from './common.js'

...

import('https://cdn.jsdelivr.net/npm/<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="25494a4144564d08405665110b14120b1410">[email&#160;protected]</a>/slice.js').then((module) =&gt; {...})
</code></pre>
<p><img src="assets/CgqCHl9yo46AYuszAANDvM6jRMk647.png" alt="Drawing 0.png" /></p>
<p>从示例中可以看到，在没有任何构建工具处理的情况下，在页面中引入带有 type=&quot;module&quot; 属性的 script，浏览器就会在加载入口模块时依次加载了所有被依赖的模块。下面我们就来深入了解一下这种基于浏览器加载 JS 模块的技术的细节。</p>
<h3>基于浏览器的 JS 模块加载功能</h3>
<p>从 caniuse 网站中可以看到，目前大部分主流的浏览器都已支持 JavaScript modules 这一特性，如下图所示：</p>
<p><img src="assets/Ciqc1F9yo5aADhYKAAMTR4GJTG8708.png" alt="Drawing 1.png" /></p>
<p>[图片来源：<a href="https://caniuse.com/es6-module">https://caniuse.com/es6-module</a>]</p>
<p>我们来总结这种加载方式的注意点。</p>
<h4>HTML 中的 Script 引用</h4>
<ul>
<li>入口模块文件在页面中引用时需要带上**type=&quot;module&quot;**属性。对应的，存在 type=&quot;nomodule&quot;，即支持 ES Module 的现代浏览器，它会忽略 type=&quot;nomodule&quot; 属性的 script，因此可以用作旧浏览器中的降级方案。</li>
<li>带有 type=&quot;module&quot; 属性的 script在浏览器中<strong>通过 defer 的方式异步执行</strong>（异步下载，不阻塞 HTML，顺次执行），即使是行内的 script 代码也遵循这一原则（而普通的行内 script 代码则忽略 defer 属性）。</li>
<li>带有 type=&quot;module&quot; 属性且带有<strong>async</strong>属性的 script，在浏览器中<strong>通过 async 的方式异步执行</strong>（异步下载，不阻塞 HTML，按该<strong>模块和所依赖的模块</strong>下载完成的先后顺序执行，无视 DOM 中的加载顺序），即使是行内的 script 代码，也遵循这一原则（而普通的行内 script 代码则忽略 async 属性）。</li>
<li>即使多次加载相同模块，也只会执行一次。</li>
</ul>
<h4>模块内依赖的引用</h4>
<ul>
<li>只能使用 import ... from '...' 的 ES6 风格的模块导入方式，或者使用 import(...).then(...) 的 ES6 动态导入方式，不支持其他模块化规范的引用方式（例如 require、define 等）。</li>
<li>导入的模块只支持使用相对路径（'/xxx', './xxx', '../xxx'）和 URL 方式（'https://xxx', 'http://xxx'）进行引用，不支持直接使用包名开头的方式（'xxxx', 'xxx/xxx'）。</li>
<li>只支持引用MIME Type为 text/javascript 方式的模块，不支持其他类型文件的加载（例如 CSS 等）。</li>
</ul>
<h4>为什么需要构建工具</h4>
<p>从上面的技术细节中我们会发现，对于一个普通的项目而言，要使用这种加载方案仍然有几个主要问题：</p>
<ol>
<li>许多其他类型的文件需要编译处理为 ES6 模块才能被浏览器正常加载（JSX、Vue、TS、CSS、Image 等）。</li>
<li>许多第三方依赖包在通过第三方 URL 引用时，不仅过程烦琐，而且往往难以进行灵活的版本控制与更新，因此需要合适的方式来解决引用路径的问题。</li>
<li>对于现实中的项目开发而言，一些便利的辅助开发技术，例如热更新等还是需要由构建工具来提供。</li>
</ol>
<p>下面，我们分析 Vite 和 Snowpack 这两个有代表性的构建工具是如何解决上面的问题的。</p>
<h3>Vite</h3>
<p><a href="https://github.com/vitejs/vite">Vite</a> 是 Vue 框架的作者尤雨溪最新推出的基于 Native-ESM 的 Web 构建工具。它在开发环境下基于 Native-ESM 处理构建过程，只编译不打包，在生产环境下则基于 Rollup 打包。我们还是先通过 Vite 的官方示例来观察它的使用效果，如下面的代码和图片所示（示例代码参见 <a href="https://github.com/fe-efficiency/lessons_fe_efficiency/tree/master/16_nobundle/example-vite">example-vite</a>）：</p>
<pre><code>npm init vite-app example-vite

cd example-vite

npm install

npm run dev
</code></pre>
<p><img src="assets/CgqCHl9yo-mAWrIzAAOaSZguuaM643.png" alt="Drawing 2.png" /></p>
<p>可以看到，运行示例代码后，在浏览器中只引入了 src/main.js 这一个入口模块，但是在网络面板中却依次加载了若干依赖模块，包括外部模块 vue 和 css。依赖图如下：</p>
<p><img src="assets/Ciqc1F9yo_GAWATTAACYUvrJKL4148.png" alt="Drawing 4.png" /></p>
<p>可以看到，经过 Vite 处理后，浏览器中加载的模块与源代码中导入的模块相比发生了变化，这些变化包括对外部依赖包的处理，对 vue 文件的处理，对 css 文件的处理等。下面我们就来逐个分析其中的变化。</p>
<h4>对导入模块的解析</h4>
<p><strong>对 HTML 文件的预处理</strong></p>
<p>当启动 Vite 时，会通过 <a href="https://github.com/vitejs/vite/blob/master/src/node/server/serverPluginHtml.ts">serverPluginHtml</a>.ts 注入 <a href="https://github.com/vitejs/vite/blob/master/src/client/client.ts">/vite/client</a> 运行时的依赖模块，该模块用于处理热更新，以及提供更新 CSS 的方法 updateStyle。</p>
<p><strong>对外部依赖包的解析</strong></p>
<p>首先是对不带路径前缀的外部依赖包（也称为<strong>Bare Modules</strong>）的解析，例如上图中在示例源代码中导入了 'vue' 模块，但是在浏览器的网络请求中变为了请求 /@module/vue。</p>
<p>这个解析过程在 Vite 中主要通过三个文件来处理：</p>
<ul>
<li><a href="https://github.com/vitejs/vite/blob/master/src/node/resolver.ts#L464">resolver</a>.ts 负责找到对应在 node_modules 中的真实依赖包代码（Vite 会在启动服务时对项目 package.json 中的 dependencies 做预处理读取并存入缓存目录 node_modules/.vite_opt_cache 中）。</li>
<li><a href="https://github.com/vitejs/vite/blob/master/src/node/server/serverPluginModuleRewrite.ts">serverPluginModuleRewrite</a>.ts 负责把源码中的 bare modules 加上 /@module/ 前缀。</li>
<li><a href="https://github.com/vitejs/vite/blob/master/src/node/server/serverPluginModuleResolve.ts">serverPluginModuleResolve</a>.ts 负责解析加上前缀后的模块。</li>
</ul>
<p><strong>对 Vue文件的解析</strong></p>
<p>对 Vue 文件的解析是通过 <a href="https://github.com/vitejs/vite/blob/master/src/node/server/serverPluginVue.ts">serverPluginVue</a>.ts 处理的，分离出 Vue 代码中的 script/template/style 代码片段，并分别转换为 JS 模块，然后将 template/style 模块的 import写到script 模块代码的头部。因此在浏览器访问时，一个 Vue 源代码文件会分裂为 2~3 的关联请求（例如上面的 /src/App.vue 和 /src/App.vue?type=template，如果 App.vue 中包含<code> &lt;style&gt;</code> 则会产生第 3 个请求 /src/App.vue?type=style）。</p>
<p><strong>对 CSS 文件的解析</strong></p>
<p>对 CSS 文件的解析是通过 <a href="https://github.com/vitejs/vite/blob/master/src/node/server/serverPluginCss.ts">serverPluginCSS</a>.ts 处理的，解析过程主要是将 CSS 文件的内容转换为下面的 JS 代码模块，其中的 updateStyle 由注入 HTML 中的 /vite/client 模块提供，如下面的代码所示：</p>
<pre><code>import { updateStyle } from &quot;/vite/client&quot;

const css = &quot;...&quot;

updateStyle(&quot;\&quot;...\&quot;&quot;, css) // id, cssContent

export default css
</code></pre>
<p>以上就是示例代码中主要文件类型的基本解析逻辑，可以看到，Vite 正是通过这些解析器来解决不同类型文件以 JS 模块的方式在浏览器中加载的问题。在 Vite 源码中还包含了其他更多文件类型的解析器，例如 JSON、TS、SASS 等，这里就不一一列举了，感兴趣的话，你可以进一步查阅<a href="https://github.com/vitejs/vite">官方文档</a>。</p>
<h4>Vite 中的其他辅助功能</h4>
<p>除了提供这些解析器的能力外，Vite 还提供了其他便捷的构建功能，大致整理如下：</p>
<ul>
<li><strong>多框架</strong>：除了在默认的 Vue 中使用外，还支持在 React 和 Preact 项目中使用。工具默认提供了 Vue、React 和 Preact 对应的脚手架模板。</li>
<li><strong>热更新（HMR）</strong>：默认提供的 3 种框架的脚手架模板中都内置了 HMR 功能，同时也提供了 HMR 的 API 供第三方插件或项目代码使用。</li>
<li><strong>自定义配置文件</strong>：支持使用自定义配置文件来细化构建配置，配置项功能参考 <a href="https://github.com/vuejs/vite/blob/master/src/node/config.ts">config.ts</a>。</li>
<li><strong>HTTPS 与 HTTP/2</strong>：支持使用 --https 启动参数来开启使用 HTTPS 和 HTTP/2 协议的开发服务器。</li>
<li><strong>服务代理</strong>：在自定义配置中支持配置代理，将部分请求代理到第三方服务。</li>
<li><strong>模式与环境变量</strong>：支持通过 mode 来指定构建模式为 development 或 production。相应模式下自动读取 dotenv 类型的环境变量配置文件（例如 .env.production.local）。</li>
<li><strong>生产环境打包</strong>：生产环境使用 Rollup 进行打包，支持传入自定义配置，配置项功能参考 <a href="https://github.com/vitejs/vite/blob/master/src/node/build/index.ts">build/index.ts</a>。</li>
</ul>
<h4>Vite 的使用限制</h4>
<p>Vite 的使用限制如下：</p>
<ul>
<li>面向支持 ES6 的现代浏览器，在生产环境下，编译目标参数 esBuildTarget 的默认值为 es2019，最低支持版本为 es2015（因为内部会使用 <a href="https://github.com/vitejs/vite/blob/master/src/node/esbuildService.ts">esbuild</a> 处理编译压缩，用来获得<a href="https://github.com/evanw/esbuild#why-is-it-fast">最快的构建速度</a>）。</li>
<li>对 Vue 框架的支持目前仅限于最新的 Vue 3 版本，不兼容更低版本。</li>
</ul>
<h3>Snowpack</h3>
<p>Snowpack 是另一个比较知名的无包构建工具，从整体功能来说和上述 Vite工具提供的功能大致相同，主要差异点在 Snowpack 在生产环境下默认使用无包构建而非打包模式（可以通过引入打包插件例如 @snowpack/plugin-webpack 来实现打包模式），而 Vite 仅在开发模式下使用。示例代码参见 <a href="https://github.com/fe-efficiency/lessons_fe_efficiency/tree/master/16_nobundle/example-vite">example-snow</a>。下面我们简单整理下两者的异同。</p>
<h4>与 Vite 相同的功能点</h4>
<p>两者都支持各种代码转换加载器、热更新、环境变量（需要安装 dotenv 插件）、服务代理、HTTPS 与 HTTP/2 等。</p>
<h4>与 Vite 的差异点</h4>
<ul>
<li><strong>相同的功能，实现细节不同</strong>：例如对 Bare Module 的处理，除了转换后前缀名称不同外（Vite 使用 /@module/ 前缀，而 Snowpack 使用 /web_modules/ 前缀)，Vite 支持类似 &quot;AAA/BBB&quot; 类型的子模块引用方式，而 Snowpack 目前尚不支持。</li>
<li><strong>工具稳定性</strong>：截止写稿的时间点（2020 年 9 月 21 日），Vite 的最新版本为 v1.0.0-rc4，仍未发布第一个稳定版本。而 Snowpack 自年初发布第一个稳定版本以来，已经更新到了 v2.11.1 版本。</li>
<li><strong>插件体系</strong>：除了版本差异外，Snowpack 提供了较完善的插件体系，支持用户和社区发布自定义插件，而 Vite 虽然也内置了许多插件，但目前并没有提供自定义插件的相关文档。</li>
<li><strong>打包工具</strong>：在生产环境下，Vite 使用 Rollup 作为打包工具，而 Snowpack 则需要引入插件来实现打包功能，官方支持的打包插件有 @snowpack/plugin-webpack 和 @snowpack/plugin-parcel，暂未提供 Rollup 对应的插件。</li>
<li><strong>特殊优化</strong>：Vite 中内置了对 Vue 的大量构建优化，因此对 Vue 项目而言，选择 Vite 通常可以获得更好的开发体验。</li>
</ul>
<h3>无包构建与打包构建</h3>
<p>通过上面的 Vite 等无包构建工具的功能介绍可以发现，同 Webpack 等主流打包构建工具相比，无包构建流程的优缺点都十分明显。</p>
<h4>无包构建的优点</h4>
<p>无包构建的最大优势在于<strong>构建速度快</strong>，尤其是启动服务的<strong>初次构建速度</strong>要比目前主流的打包构建工具要快很多，原因如下：</p>
<ul>
<li><strong>初次构建启动快</strong>：打包构建流程在初次启动时需要进行一系列的模块依赖分析与编译，而在无包构建流程中，这些工作都是<strong>在浏览器渲染页面时异步处理的</strong>，启动服务时只需要做少量的优化处理即可（例如缓存项目依赖的 Bare Modules），所以启动非常快。</li>
<li><strong>按需编译</strong>：在打包构建流程中，启动服务时即需要完整编译打包所有模块，而无包构建流程是在浏览器渲染时，根据入口模块分析加载所需模块，编译过程按需处理，因此相比之下处理内容更少，速度也会更快</li>
<li><strong>增量构建速度快</strong>：在修改代码后的 rebuild 过程中，主流的打包构建中仍然包含编译被修改的模块和打包产物这两个主要流程，因此相比之下，只需处理编译单个模块的无包构建在速度上也会更胜一筹（尽管在打包构建工具中，也可以通过分包等方式尽可能地减少两者的差距）。</li>
</ul>
<h4>无包构建的缺点</h4>
<ul>
<li><strong>浏览器网络请求数量剧增</strong>：无包构建最主要面对的问题是，它的运行模式决定了在一般项目里，渲染页面所需发起的请求数远比打包构建要多得多，使得打开页面会产生瀑布式的大量网络请求，将对页面的渲染造成延迟。这对于服务稳定性和访问性能要求更高的生产环境而言，通常是不太能接受的，尤其对不支持 HTTP/2 的服务器而言，这种处理更是灾难性的。因此，一般是在开发环境下才使用无包构建，在生产环境下则仍旧使用打包构建。</li>
<li><strong>浏览器的兼容性</strong>：无包构建要求浏览器支持 JavaScript module 特性，尽管目前的主流浏览器已大多支持，但是对于需要兼容旧浏览器的项目而言，仍然不可能在生产环境下使用。而在开发环境下则通常没有这种顾虑。</li>
</ul>
<h3>总结</h3>
<p>这节课我们主要讨论了今年比较热门的无包构建。</p>
<p>无包构建产生的基础是浏览器对 JS 模块加载的支持，这样才可能把构建过程中分析模块依赖关系并打包的过程变为在浏览器中逐个加载引用的模块。但是这种加载模块的方式在实际项目应用场景下还存在一些阻碍，于是有了无包构建工具。</p>
<p>在这些工具里，我们主要介绍了 Vite 和 Snowpack，希望通过介绍他们的开发模式的基本工作流程和差异点，让你对这类工具的功能特点有一个基本的了解。</p>
<p>今天的课后思考题是，为什么 Vite/Snowpack 这样的无包构建工具要比 Webpack 这样的打包构建工具速度更快呢？</p>
<p>随着这节课的结束，构建优化模块也就告一段落了。下节课开始我们将进入部署优化模块。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="15&#32;&#32;版本特性：Webpack&#32;5&#32;中的优化细节.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="17&#32;&#32;部署初探：为什么一般不在开发环境下部署代码？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43521c1c37645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E5%89%8D%E7%AB%AF%E5%B7%A5%E7%A8%8B%E5%8C%96%E7%B2%BE%E8%AE%B2-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
