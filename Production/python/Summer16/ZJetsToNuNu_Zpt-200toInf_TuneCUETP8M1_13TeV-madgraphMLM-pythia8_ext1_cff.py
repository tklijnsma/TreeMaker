import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/0ADB28CD-36E2-E611-B74D-FA163EE54EB5.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/12D405E6-25E3-E611-A7D6-24BE05CECBD1.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/1E9D6732-25E3-E611-B810-A0369FC5D904.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/26E684AC-2DE3-E611-9A64-90B11C08C1BA.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/38A8E831-5DE2-E611-8133-FA163E275D07.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/4639D41F-D9E3-E611-995B-ECF4BBE16468.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/46AEC26A-26E3-E611-8A21-1C6A7A21A73B.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/48315D1C-30E5-E611-9CCA-842B2B181671.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/4AAD2692-00E4-E611-AE32-008CFA111244.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/4E6119D1-98E4-E611-B46F-00259048BF92.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/5CAEEE6B-06E3-E611-A281-FA163E753725.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/5EE0CE90-F9E3-E611-99CC-001E67DFF7CB.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/6E9189B2-D0F1-E611-B809-02163E011C22.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/74DE81C0-DFE3-E611-A8EF-549F3525B154.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/7A4F422C-CEE3-E611-8904-FA163ECF6C9D.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/804799A7-26E3-E611-9E4F-008CFA110B10.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/841BA5E6-F3E3-E611-ABD3-A0369FC5FBA4.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/86DCC2BA-36E2-E611-8151-FA163E132292.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/90685CC2-36E2-E611-A4E9-FA163E1E1B94.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/9A38A42B-4BE3-E611-93B8-0025905A6066.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/9AA99594-16E3-E611-A13C-001E67DDBFF7.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/9C1BF887-E8F1-E611-93A3-02163E013412.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/A448DF7F-9DE2-E611-AF5B-B8CA3A709028.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/AA3A9B66-15E4-E611-B781-0CC47A4D766C.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/B0B7FA2B-4BE3-E611-9C35-0025905A48F0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/B25C0F64-15E4-E611-9B29-0025905A6064.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/C0BD9214-1EE3-E611-9946-00266CFCCB44.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/C8BA49DF-E6E3-E611-A5AF-44A84224BE51.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/DAF85FE8-6CE4-E611-B149-24BE05C44B91.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/DED2B8D7-9CE3-E611-8519-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/E0F03F0D-D4E3-E611-AFEB-FA163EE8E187.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/E87DC8B2-DAF1-E611-9CEB-02163E019E2F.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/EA8FA552-35E3-E611-9325-008CFA111314.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/EC152498-3AE2-E611-9C52-001E67C9B39D.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/F00E083F-3AE2-E611-93DD-001E67C9B39D.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/F0966369-26E3-E611-ACA1-0CC47AA98A0E.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/FA2600C4-ACE4-E611-8F1B-02163E013D9B.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/FA769DE3-CCE4-E611-B210-0090FAA585D4.root',
] )
