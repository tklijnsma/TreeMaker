import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/584/00000/8A5B7CB0-855D-E511-BFCF-02163E0133A9.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/587/00000/F664AC07-935D-E511-A019-02163E01424B.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/629/00000/6EDCF302-0A5F-E511-A5EF-02163E014642.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/630/00000/86ACFECD-3C5F-E511-B8F2-02163E014374.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/662/00000/300565D4-F55E-E511-95AF-02163E011D25.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/672/00000/0C762538-075F-E511-ACEE-02163E0136C1.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/673/00000/F20A98EE-1C5F-E511-8845-02163E014767.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/674/00000/DA9B86E1-F95E-E511-B75E-02163E013460.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/675/00000/6467F0A5-A75F-E511-AE8A-02163E013389.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/675/00000/7285B0A0-A75F-E511-8C73-02163E011911.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/675/00000/D68BBF9F-A75F-E511-9D37-02163E011BD2.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/676/00000/1069ABF5-C15F-E511-898B-02163E014160.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/676/00000/206851F5-C15F-E511-A5A5-02163E0142BA.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/676/00000/2A98DEF6-C15F-E511-B5F9-02163E012A2E.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/676/00000/36C1F29D-C25F-E511-B94E-02163E011F85.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/676/00000/3A2126E4-C15F-E511-A4D2-02163E011888.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/676/00000/506D1AE8-C15F-E511-8A08-02163E0144EA.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/676/00000/5CC9C1EC-C15F-E511-9417-02163E014370.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/676/00000/62B3323F-C35F-E511-B49D-02163E0143A2.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/676/00000/866DBCDD-C15F-E511-B4DE-02163E013965.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/676/00000/C0DE1AED-C15F-E511-971C-02163E014337.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/676/00000/C4318ED7-C15F-E511-91C0-02163E012175.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/676/00000/EC93F0E5-C15F-E511-940F-02163E01350C.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/676/00000/EEE0E0DD-C15F-E511-A1FD-02163E014268.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/677/00000/58B82BAD-985F-E511-AA44-02163E012386.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/677/00000/5E2C8E5D-985F-E511-A44D-02163E013394.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/677/00000/9C98C472-985F-E511-8D21-02163E013724.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/677/00000/CE704966-985F-E511-BD46-02163E01371D.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/677/00000/F6175162-985F-E511-9C98-02163E012254.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/721/00000/4A39D05B-0A5F-E511-A441-02163E0133EB.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/725/00000/284B4806-395F-E511-B1FE-02163E013857.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/727/00000/949DCD59-925F-E511-AAB0-02163E01198C.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/728/00000/6CD0D371-415F-E511-B424-02163E014337.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/02D54307-4B60-E511-837F-02163E014144.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/08979DAA-4460-E511-94A0-02163E011D99.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/0AF27211-4760-E511-B119-02163E01393A.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/0E2E5F90-4660-E511-8ACF-02163E0139AF.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/1C0A4637-4C60-E511-ADD0-02163E011B5E.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/1E8BEB91-4660-E511-9E6D-02163E01396A.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/286EC6C1-4460-E511-B112-02163E0133F2.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/36341524-5660-E511-B81B-02163E0144EA.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/48DD2D2D-4C60-E511-B346-02163E01393A.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/4EB760E9-4560-E511-9B26-02163E01393A.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/4EDD20B1-4760-E511-8759-02163E011B0F.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/5C3E0500-4B60-E511-985F-02163E0142C8.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/6E916AE5-4560-E511-B63E-02163E014327.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/700F6959-4960-E511-BC32-02163E0142A4.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/7A0CA7E5-4560-E511-B868-02163E014327.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/7C65D6E4-4360-E511-80B0-02163E014144.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/8A630C0B-4560-E511-A0C8-02163E014734.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/8EF007AC-4460-E511-853C-02163E0133FC.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/90DD7FE6-4360-E511-A03A-02163E013635.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/926FA510-4760-E511-9375-02163E011842.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/A222235A-4960-E511-AEA7-02163E011D99.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/A2BA808F-4660-E511-AE0C-02163E014408.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/A8DBDF0A-4560-E511-987B-02163E01451A.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/BE365695-4660-E511-ADB1-02163E014422.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/C2A7C8EA-4560-E511-BED1-02163E011BFC.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/D077D8A8-4460-E511-A265-02163E01457E.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/D0DBC2E0-4560-E511-808E-02163E011BB3.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/DC2E8190-4660-E511-B084-02163E0138C1.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/DCA65018-4560-E511-90EF-02163E011C09.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/DE64C510-4560-E511-BD67-02163E012968.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/729/00000/F631EFE7-4F60-E511-B403-02163E014750.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/734/00000/184C3E0F-4D60-E511-AC79-02163E011EA7.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/734/00000/34395710-4D60-E511-9C6C-02163E014234.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/734/00000/76ED750F-4D60-E511-8243-02163E014353.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/734/00000/9C2A641D-4D60-E511-A757-02163E01338B.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/798/00000/306EF744-B15F-E511-B59D-02163E011F46.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/801/00000/3A402827-6C60-E511-B0C3-02163E0145DA.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/801/00000/946AE229-6C60-E511-893D-02163E01444F.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/801/00000/D007CB26-6C60-E511-B3E3-02163E0140D9.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/801/00000/D02F582B-6C60-E511-B3E8-02163E011F42.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/801/00000/FE0F1538-6C60-E511-BAA5-02163E0133A4.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/834/00000/7EEF9E56-0060-E511-8D6A-02163E0141AC.root',
       '/store/data/Run2015D/JetHT/MINIAOD/PromptReco-v3/000/256/842/00000/2A7065F1-6260-E511-9C8D-02163E0141BE.root' ] );


secFiles.extend( [
               ] )

