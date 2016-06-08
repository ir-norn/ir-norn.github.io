
#coding:utf-8
require 'webrick'
require "socket"
require "webrick/ssl"

#Encoding.default_external = "UTF-8"
#$localip = IPSocket::getaddress(Socket::gethostname)

srv = WEBrick::HTTPServer.new( {
  :ServerName     => "Server", # WEBrick::Utils.getservername
  :BindAddress    => $localip || "127.0.0.1" ,
  :Port           => 8050,
  :MaxClients     => 100,   # maximum number of the concurrent connections
#  :ServerType     => WEBrick::Daemon,
  :ServerType     => nil,   # default: WEBrick::SimpleServer
  :Logger         => nil,   # default: WEBrick::Log.new
  :ServerSoftware => "WEBrick/#{WEBrick::VERSION} " +
                     "(Ruby/#{RUBY_VERSION}/#{RUBY_RELEASE_DATE})",
  :TempDir        => ENV['TMPDIR']||ENV['TMP']||ENV['TEMP']||'/tmp',
  :DoNotListen    => false,
  :StartCallback  => nil,
  :StopCallback   => nil,
  :AcceptCallback => nil,
  :DoNotReverseLookup => nil,

  :RequestTimeout => 30,
#  :HTTPVersion    => HTTPVersion.new("1.1"),
  :AccessLog      => nil,
  :MimeTypes      => WEBrick::HTTPUtils::DefaultMimeTypes,
  :DirectoryIndex => [ "index.cgi" ,"index.html","index.htm","index.rhtml"],
  :DocumentRoot   => "C:/xxx/gh/ir-norn.github.io/",
#  :DocumentRoot   => "./",
  :DocumentRootOptions => { :FancyIndexing => true },
  :RequestCallback => nil,
  :ServerAlias    => nil,

  :CGIInterpreter => 'C:\ruby\bin\ruby.exe',
  :CGIPathEnv     => nil,

  # workaround: if Request-URIs contain 8bit chars,
  # they should be escaped before calling of URI.parse().
  :Escape8bitURI  => false

#  :SSLEnable  => true
})

trap('INT') { server.shutdown }

#res = WEBrick::HTTPResponse.new( { :HTTPVersion => "1.1" } )
#res.status = 404
#p res.reason_phrase    #=> "Not Found"

if not defined?(Ocra)
   srv.start
end
