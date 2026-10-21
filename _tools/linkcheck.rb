# frozen_string_literal: true
# encoding: utf-8
require "uri"

ROOT = ENV.fetch("SITE_DIR", "_site")
files = Dir.glob("#{ROOT}/**/*.html") + Dir.glob("#{ROOT}/**/*.xml")
broken = []
checked = 0

files.each do |f|
  html = File.read(f, encoding: "utf-8")
  base = ROOT.length
  ids = html.scan(/id="([^"]+)"/).flatten

  html.scan(%r{(?:href|src)="([^"]+)"}).flatten.each do |t|
    next if t.nil? || t.empty?
    next if t =~ %r{\A(https?:|//|mailto:|data:|#)}
    next unless t.start_with?("/")

    checked += 1
    path, raw_frag = t.split("#", 2)
    path = URI.decode_www_form_component(path.to_s).sub(%r{\A/}, "")
    frag = raw_frag.nil? ? nil : URI.decode_www_form_component(raw_frag)

    resolved =
      if path.empty?
        "#{ROOT}/index.html"
      elsif path.end_with?("/")
        "#{ROOT}/#{path}index.html"
      else
        "#{ROOT}/#{path}"
      end

    unless File.exist?(resolved)
      broken << "#{f}: #{t} -> MISSING #{resolved}"
      next
    end

    if frag && !frag.empty? && resolved.end_with?(".html")
      doc = File.read(resolved, encoding: "utf-8")
      doc_ids = doc.scan(/id="([^"]+)"/).flatten
      broken << "#{f}: #{t} -> no id '#{frag}'" unless doc_ids.include?(frag)
    end
  end

  # 同页锚点
  html.scan(%r{href="#([^"]+)"}).flatten.each do |frag|
    checked += 1
    broken << "#{f}: ##{frag} -> no such id on page" unless ids.include?(frag)
  end
end

puts "html files=#{Dir.glob("#{ROOT}/**/*.html").size} links checked=#{checked} broken=#{broken.size}"
broken.first(15).each { |b| puts "  #{b}" }
exit(broken.empty? ? 0 : 1)
